import os
import sys
sys.path.append('src')
from src.logger.logging import logging
from src.exception.exception import customeexception
import pandas as pd

from src.componemts.data_ingestion import DataIngestion
from src.componemts.data_transformation import DataTransformation
from src.componemts.model_trainer import ModelTrainer
from src.componemts.model_evaluation import ModelEvaluation


obj = DataIngestion()

train_data_path, test_data_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()

train_arr, test_arr = data_transformation.initialize_data_transformation(
    train_data_path, test_data_path
)


model_trainer_obj = ModelTrainer()
model_trainer_obj.initate_model_training(train_arr, test_arr)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr, test_arr)