from datascience.config.configuration import configuration_manager
from datascience.components.data_validation import DataValiadtion
from datascience.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = configuration_manager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            validation_status = data_validation.validate_all_files_exist()
            logger.info(f"Data validation status: {validation_status}")
        except Exception as e:
            logger.error(f"Error during data validation: {e}")
            raise e