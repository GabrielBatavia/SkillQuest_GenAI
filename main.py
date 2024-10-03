import neptune
import os
from config.config import paths_config
from training import fine_tune_and_save_model
from transformers import AutoModelForCausalLM, AutoTokenizer

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

run = neptune.init_run(
    project="SkillQuest/SkillQuest",
    api_token="your_api_token_here",
    name="Production Fine-tuning Nusantara Chat Model",
    tags=["fine-tuning", "NLP", "Transformers", "production"],
    dependencies="infer",
    capture_hardware_metrics=True,
)

local_train_file = paths_config["train_file"]
local_eval_file = paths_config["eval_file"]
local_output_dir = paths_config["output_dir"]

local_root_file = paths_config["root_words_file"]
local_slang_file = paths_config["slang_words_file"]
local_stop_file = paths_config["stop_words_file"]

def validate_saved_model(output_dir):
    try:
        model = AutoModelForCausalLM.from_pretrained(output_dir)
        tokenizer = AutoTokenizer.from_pretrained(output_dir)
        print("Model and tokenizer successfully loaded.")
    except Exception as e:
        print(f"Failed to load the model or tokenizer from {output_dir}. Error: {e}")

def main(production_params, trial_number=None, save_model=True):
    trial_output_dir = f"{local_output_dir}/trial_{trial_number}" if trial_number is not None else local_output_dir

    train_loss, total_words, total_values = fine_tune_and_save_model(
        model_name="kalisai/Nusantara-2.7b-Indo-Chat",
        train_file=local_train_file,
        eval_file=local_eval_file,
        output_dir=trial_output_dir,
        params=production_params,
        vocab_txt_file=[local_root_file, local_stop_file],
        vocab_json_file=local_slang_file,
        run=run,
        save_model=save_model
    )

    print(f"Total words added to tokenizer: {total_words}")
    print(f"Total human and GPT conversation values loaded: {total_values}")

    if save_model:
        print("Training complete, and model saved.")
        validate_saved_model(trial_output_dir)
    else:
        print("Training complete, model not saved.")

    return train_loss

if __name__ == "__main__":
    use_optuna = False

    if use_optuna:
        from optuna_opt import run_optuna
        run_optuna(lambda params, trial_number: main(params, trial_number, save_model=False))
    else:
        production_params = {
            "batch_size": 24,
            "num_train_epochs": 200,
            "learning_rate": 5e-5,
            "gradient_accumulation_steps": 8,
            "optimizer": "AdamW"  # Switch to AdamW optimizer
        }
        main(production_params, save_model=True)

    run.stop()
