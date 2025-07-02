from datascience.constants import *
from datascience.utils.common import read_yaml, create_directories
from datascience.entity import DataIngestionConfig

class configuration_manager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns Data Ingestion Configuration
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir, config.unzip_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            locate_data_file=Path(config.locate_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        return data_ingestion_config