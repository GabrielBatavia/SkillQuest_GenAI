import neptune
import os
from config.config import paths_config
from training import fine_tune_and_save_model
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set environment variable to handle memory fragmentation
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# Initialize Neptune for logging
run = neptune.init_run(
    project="SkillQuest/SkillQuest",
    api_token="your_api_token_here",
    name="Production Fine-tuning Nusantara Chat Model",
    tags=["fine-tuning", "NLP", "Transformers", "production"],
    dependencies="infer",
    capture_hardware_metrics=True,
)

# Load paths from config
local_train_file = paths_config["train_file"]
local_eval_file = paths_config["eval_file"]
local_output_dir = paths_config["output_dir"]

# Paths for additional vocabulary files
local_root_file = paths_config["root_words_file"]
local_slang_file = paths_config["slang_words_file"]
local_stop_file = paths_config["stop_words_file"]

def validate_saved_model(output_dir):
    """
    Validate if the model and tokenizer can be loaded successfully after training.
    """
    try:
        model = AutoModelForCausalLM.from_pretrained(output_dir)
        tokenizer = AutoTokenizer.from_pretrained(output_dir)
        print("Model and tokenizer successfully loaded.")
    except Exception as e:
        print(f"Failed to load the model or tokenizer from {output_dir}. Error: {e}")

def main(production_params, trial_number=None, save_model=True):
    """
    Main function for fine-tuning the model and handling trial outputs if necessary.
    """
    trial_output_dir = f"{local_output_dir}/trial_{trial_number}" if trial_number is not None else local_output_dir

    # Fine-tune the model and save it
    train_loss, total_words, total_values = fine_tune_and_save_model(
        model_name="kalisai/Nusantara-2.7b-Indo-Chat",
        train_file=local_train_file,
        eval_file=local_eval_file,
        output_dir=trial_output_dir,
        params=production_params,  # Use parameters provided in main
        vocab_txt_file=[local_root_file, local_stop_file],  # Provide both txt files as a list
        vocab_json_file=local_slang_file,
        run=run,  # Log with Neptune
        save_model=save_model  # Specify if the model should be saved
    )

    # Output relevant information after training
    print(f"Total words added to tokenizer: {total_words}")
    print(f"Total human and GPT conversation values loaded: {total_values}")

    if save_model:
        print("Training complete, and model saved.")
        validate_saved_model(trial_output_dir)
    else:
        print("Training complete, model not saved.")

    return train_loss

if __name__ == "__main__":
    use_optuna = False  # Set to True if Optuna should be used for hyperparameter tuning

    if use_optuna:
        from optuna_opt import run_optuna  # Import Optuna optimization if needed
        run_optuna(lambda params, trial_number: main(params, trial_number, save_model=False))
    else:
        # Define production parameters for fine-tuning
        production_params = {
            "batch_size": 24,
            "num_train_epochs": 10,
            "learning_rate": 5e-5,
            "gradient_accumulation_steps": 8,
            "optimizer": "SGD"  # Specify optimizer
        }
        main(production_params, save_model=True)

    run.stop()
