import os
from datascience.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from datascience.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        
    def convert_examples_to_features(self, example_batch):
        judgements = [str(j) if j is not None else "" for j in example_batch['judgement']]
        summaries = [str(s) if s is not None else "" for s in example_batch['summary']]
        input_encodings = self.tokenizer(judgements, max_length=1024, truncation=True)
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(summaries, max_length=128, truncation=True)
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    

    def convert(self):
        dataset_legal = load_dataset("csv",data_files={
            "train": "artifacts/data_ingestion/train_dataset.csv",
            "test": "artifacts/data_ingestion/test_dataset.csv"
            }
                                     )
        dataset_legal_pt = dataset_legal.map(self.convert_examples_to_features, batched = True)
        dataset_legal_pt.save_to_disk(os.path.join(self.config.root_dir,"legal_summary"))