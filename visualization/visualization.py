import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import torch
import random

def plot_attention_heatmap(attention_scores, input_tokens, output_tokens, example_idx, cmap='viridis', annot=False, color_bar=True, vmin=None, vmax=None):
    """
    Generate and save a heatmap visualization of attention scores for a specific example in a sequence-to-sequence model.
    """
    truncated_output_tokens = output_tokens[:attention_scores.shape[0]]
    attention_scores = attention_scores[:len(truncated_output_tokens), :len(input_tokens)]
    df = pd.DataFrame(attention_scores, index=truncated_output_tokens, columns=input_tokens[:len(input_tokens)])

    plt.figure(figsize=(15, 10))
    sns.heatmap(df, annot=annot, cmap=cmap, cbar=color_bar, vmin=vmin, vmax=vmax)
    plt.xlabel("Input Tokens")
    plt.ylabel("Output Tokens")
    plt.title(f"Attention Heatmap Example {example_idx + 1}")
    plt.tight_layout()
    plt.savefig(f"attention_heatmap_example_{example_idx + 1}_{cmap}_annot_{annot}.png")
    plt.close()

    print(f"Attention heatmap for example {example_idx + 1} saved.")

def visualize_random_samples_attention(model, tokenizer, eval_data, num_samples=3):
    """
    Select random samples from the evaluation data, generate model predictions, and visualize the attention mechanisms using heatmaps.
    """
    for i in range(num_samples):
        sample = random.choice(eval_data)
        human_input = sample['conversations'][0]['value']
        gpt_output = sample['conversations'][1]['value']

        inputs = tokenizer(human_input, return_tensors='pt', truncation=True, padding='max_length', max_length=128)
        inputs = {key: val.to(model.device) for key, val in inputs.items()}

        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=50, pad_token_id=tokenizer.eos_token_id,
                                     output_attentions=True, return_dict_in_generate=True)

        decoded_pred = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        print(f"--- Sample {i + 1} ---")
        print("Human Input:")
        print(human_input)
        print("\nModel Output (Prediction):")
        print(decoded_pred)
        print("\nExpected Output:")
        print(gpt_output)
        print("\n" + "-" * 50 + "\n")

        attentions = outputs.attentions[-1][0][0].detach().cpu().numpy()
        input_tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
        output_tokens = tokenizer.convert_ids_to_tokens(outputs.sequences[0].squeeze())

        plot_attention_heatmap(attentions, input_tokens, output_tokens, i)

def plot_combined_learning_fbert(training_logs, fbert_scores):
    """
    Plots the combined learning curve and FBERT score evolution in a single figure.
    """
    epochs = range(1, len(training_logs) + 1)
    train_losses = [log['loss'] for log in training_logs]
    eval_losses = [log['eval_loss'] for log in training_logs]

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss', color='tab:blue')
    ax1.plot(epochs, train_losses, label='Training Loss', color='tab:blue', linestyle='-')
    ax1.plot(epochs, eval_losses, label='Validation Loss', color='tab:cyan', linestyle='--')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('FBERT Score', color='tab:red')
    ax2.plot(epochs, fbert_scores, label='FBERT Score', color='tab:red', linestyle=':')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.tight_layout()
    plt.title('Combined Learning Curve and FBERT Score Evolution')
    fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
    plt.show()

def plot_token_length_distribution(data, title='Token Length Distribution', color='skyblue'):
    """
    Plots a histogram showing the distribution of token lengths in the dataset.
    """
    input_lengths = [len(conv['conversations'][0]['value'].split()) for conv in data]
    output_lengths = [len(conv['conversations'][1]['value'].split()) for conv in data]

    plt.figure(figsize=(10, 5))
    plt.hist(input_lengths, bins=20, alpha=0.7, label='Input Lengths', color=color)
    plt.hist(output_lengths, bins=20, alpha=0.7, label='Output Lengths', color='salmon')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.legend()
    plt.show()
