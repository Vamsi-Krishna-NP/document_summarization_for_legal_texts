from datascience.config.configuration import configuration_manager
from datascience.components.data_ingestion import DataIngestion
from datascience.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = configuration_manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()