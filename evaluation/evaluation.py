import torch
from bert_score import score as bert_score

def decode_and_append(tokenizer, outputs, decoded_preds, gpt_output, decoded_labels):
    """Helper function to decode model output and append to lists."""
    decoded_pred = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    decoded_preds.append(decoded_pred)
    decoded_labels.append(gpt_output)

def evaluate_model_on_all_validation_data(model, tokenizer, eval_data):
    """Function to evaluate the model on validation data."""
    model.eval()  # Set model to evaluation mode
    decoded_preds = []
    decoded_labels = []
    attention_data = []

    for idx, entry in enumerate(eval_data):
        human_input = None
        gpt_output = None

        for conv in entry['conversations']:
            if conv['from'] == 'human':
                human_input = conv['value']
            elif conv['from'] == 'gpt':
                gpt_output = conv['value']

        # Ensure human_input and gpt_output are defined
        if human_input is not None and gpt_output is not None:
            inputs = tokenizer(human_input, return_tensors='pt', truncation=True, padding='max_length', max_length=128)
            inputs = {key: val.to(model.device) for key, val in inputs.items()}  # Move to the same device as the model

            with torch.no_grad():
                outputs = model.generate(**inputs, max_new_tokens=50, pad_token_id=tokenizer.eos_token_id,
                                         output_attentions=True, return_dict_in_generate=True)

            decode_and_append(tokenizer, outputs, decoded_preds, gpt_output, decoded_labels)

            attentions = outputs.attentions
            attention_scores = attentions[-1][0].squeeze().detach().cpu().numpy()  # (seq_len, seq_len)
            input_tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
            output_tokens = tokenizer.convert_ids_to_tokens(outputs.sequences[0].squeeze())
            attention_data.append((attention_scores, input_tokens, output_tokens, idx))
        else:
            print(f"Skipping example {idx + 1} due to missing human or gpt output.")

    P, R, F1 = bert_score(decoded_preds, decoded_labels, lang="id", rescale_with_baseline=True)
    avg_fbert_score = torch.mean(F1).item()

    return avg_fbert_score, F1.tolist()
