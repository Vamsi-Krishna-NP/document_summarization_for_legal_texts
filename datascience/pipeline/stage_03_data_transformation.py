from datascience.config.configuration import configuration_manager
from datascience.components.data_transformation import DataTransformation
from datascience.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = configuration_manager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
            
        except Exception as e:
            logger.error(f"Error during data Transformation: {e}")
            raise e