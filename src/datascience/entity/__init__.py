from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data Ingestion Configuration
    """
    root_dir: Path
    source_URL: str
    locate_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration for data validation.
    """
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    
@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Data Transformation Configuration
    """
    root_dir: Path
    data_path: Path
    tokenizer_name: Path