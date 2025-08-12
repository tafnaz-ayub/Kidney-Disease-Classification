from cnnClassfier import logger
from cnnClassfier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassfier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassfier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassfier.pipeline.stage_04_model_evaluation import EvaluationPipeline
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")        
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()        
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()        
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Evaluation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e