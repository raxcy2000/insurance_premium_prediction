## command + shift + P --> select interpreter --> choose interpreter

import os
#os.environ['OPENBLAS_NUM_THREADS'] = '5'

import pandas as pd
import numpy as np




from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularDataset, TabularPredictor


FILE_NAME = "insurance.csv"
DATA_FOLDER = "data"

main_path = os.getcwd()
file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), FILE_NAME)

insurance_data = pd.read_csv(file_path)

print(insurance_data[0:5])

train_data, test_data = train_test_split(insurance_data, test_size=0.33, random_state=42)
print("train_data.shape, test_data.shape", train_data.shape, test_data.shape)

label = 'charges'

save_path = 'models'
predictor = TabularPredictor(label=label, path=save_path).fit(test_data,
 excluded_model_types = ['KNN','XT','RF'], hyperparameters = 'light', presets="ignore_text")# , presets="best_quality")

print(predictor)
print(predictor.leaderboard(silent=True))