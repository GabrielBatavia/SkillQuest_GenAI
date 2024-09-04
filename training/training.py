import os
import torch
from transformers import Trainer, TrainingArguments, AutoTokenizer, DataCollatorForLanguageModeling
from utils.dataset_utils import CustomDataset
from utils.model_utils import load_model, load_dataset, load_additional_vocab
from torch.optim import SGD, RMSprop, Adagrad

def get_device():
    """Function to get the device type: GPU or CPU."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def choose_optimizer(optimizer_name, model, lr):
    """Function to choose optimizer based on a string input."""
    optimizers = {
        "SGD": SGD(model.parameters(), lr=lr, momentum=0.9),
        "RMSprop": RMSprop(model.parameters(), lr=lr, alpha=0.99),
        "Adagrad": Adagrad(model.parameters(), lr=lr)
    }
    return optimizers.get(optimizer_name, SGD(model.parameters(), lr=lr, momentum=0.9))

def fine_tune_and_save_model(model_name, train_file, eval_file, output_dir, params, vocab_txt_file=None, vocab_json_file=None, run=None, save_model=True, stop_loss_threshold=0.4):
    """Function to fine-tune and save the model."""
    device = get_device()

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Load and add additional vocabulary
    if vocab_txt_file and vocab_json_file:
        additional_vocab = load_additional_vocab(vocab_txt_file[0], vocab_txt_file[1], vocab_json_file)
        num_added_toks = tokenizer.add_tokens(additional_vocab)
        print(f"Added {num_added_toks} tokens to the tokenizer")
        print(f"Total tokens in tokenizer now: {len(tokenizer)}")

    model = load_model(model_name).to(device)
    model.gradient_checkpointing_enable()

    if vocab_txt_file and vocab_json_file and num_added_toks > 0:
        model.resize_token_embeddings(len(tokenizer))
        print("Resized model embeddings to match the new tokenizer length.")

    # Verify parameter initialization
    for name, param in model.named_parameters():
        if param.requires_grad:
            if torch.isnan(param).any():
                print(f"Warning: Parameter {name} contains NaN values.")
            if param.data.abs().sum() == 0:
                print(f"Warning: Parameter {name} has not been initialized correctly (all zeros).")

    train_data = load_dataset(train_file)

    total_values = sum(len(conv['conversations']) for conv in train_data)

    train_inputs = tokenizer([conv['conversations'][0]['value'] for conv in train_data], return_tensors='pt',
                             truncation=True, padding='max_length', max_length=128).to(device)
    train_labels = tokenizer([conv['conversations'][1]['value'] for conv in train_data], return_tensors='pt',
                             truncation=True, padding='max_length', max_length=128).to(device)

    train_dataset = CustomDataset(train_inputs, train_labels)

    model_output_dir = os.path.join(output_dir, f"SkillQuest_AI_{model_name.replace('/', '_')}")

    training_args = TrainingArguments(
        output_dir=model_output_dir,
        per_device_train_batch_size=params["batch_size"],
        gradient_accumulation_steps=params["gradient_accumulation_steps"],
        num_train_epochs=params["num_train_epochs"],
        learning_rate=params["learning_rate"],
        save_steps=10000,
        save_total_limit=2,
        logging_strategy="epoch",
        evaluation_strategy="epoch",
        save_strategy="no",
        logging_dir='./logs',
        report_to="none",
        metric_for_best_model="f1",
        fp16=torch.cuda.is_available() and device.type == 'cuda',
        load_best_model_at_end=True,
        disable_tqdm=False,
    )

    # Choose optimizer
    optimizer = choose_optimizer(params["optimizer"], model, params["learning_rate"])

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
        optimizers=(optimizer, None)
    )

    # Training with early stopping condition based on loss threshold
    for epoch in range(params["num_train_epochs"]):
        trainer.train()

        try:
            train_loss = trainer.state.log_history[-1].get('loss', None)
            if train_loss is not None:
                print(f"Epoch: {epoch}, Loss: {train_loss}")

                if train_loss < stop_loss_threshold:
                    print(f"Stopping training early as loss {train_loss} is below the threshold {stop_loss_threshold}.")
                    break

                if run is not None:
                    run[f"train/loss_epoch_{epoch}"].log(train_loss)
            else:
                raise ValueError(f"Loss not found for epoch {epoch}")

        except Exception as e:
            print(f"Error during training at epoch {epoch}: {e}")
            print("Saving the model immediately due to an error or missing loss.")
            if save_model:
                save_model_full(model, tokenizer, model_output_dir)
            return train_loss, len(tokenizer), total_values

    # Save model after successful training
    if save_model:
        save_model_full(model, tokenizer, model_output_dir)

    return train_loss, len(tokenizer), total_values

def save_model_full(model, tokenizer, model_output_dir):
    """Function to save model and tokenizer."""
    try:
        model.save_pretrained(model_output_dir)
        tokenizer.save_pretrained(model_output_dir)
        print(f"Model and tokenizer saved successfully to {model_output_dir}")
    except Exception as e:
        print(f"Failed to save the entire model or tokenizer. Error: {e}")
