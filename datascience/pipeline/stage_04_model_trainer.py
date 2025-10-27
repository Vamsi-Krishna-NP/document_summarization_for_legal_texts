from datascience.config.configuration import configuration_manager
from datascience.components.model_trainer import ModelTrainer
from datascience.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = configuration_manager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            logger.error(f"Error during Model Training: {e}")
            raise e