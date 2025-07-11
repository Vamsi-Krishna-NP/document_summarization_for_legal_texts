from datascience.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from datascience.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from datascience.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from datascience.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from datascience.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    pipeline = ModelTrainerTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e