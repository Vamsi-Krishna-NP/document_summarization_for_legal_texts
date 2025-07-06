from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datascience.config.configuration import ModelTrainerConfig
from datasets import load_dataset, load_from_disk
import os
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        
        #os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Optional: disables GPU usage

        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_t5_small = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_t5_small)
        
        # loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10, save_steps=1e6,
            gradient_accumulation_steps=16
        ) 

        trainer = Trainer(
            model=model_t5_small, args=trainer_args,
            tokenizer=tokenizer, data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"]
        )
        
        trainer.train()
        
        # Save model and tokenizer
        model_t5_small.save_pretrained(os.path.join(self.config.root_dir, "t5-legal-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))