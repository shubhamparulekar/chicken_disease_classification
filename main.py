from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

dataingestion = DataIngestionTrainingPipeline()
dataingestion.main()
