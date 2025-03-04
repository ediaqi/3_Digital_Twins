import json
import os

import pandas as pd
import torch
import torch.nn as nn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV

import settings 
from training.LSTM_model import create_lstm_model


class Hyperparameter_optimization:

    def __init__(self, X_train, X_train_scaled, y_train, X_test, X_test_scaled, y_test):

        self.models = {}
        self.results = {}
        self.predictions = {}
        self.target = None

        self.X_train = X_train
        self.X_train_scaled = X_train_scaled 
        self.y_train = y_train
        self.y_test = y_test

        self.X_test = X_test
        self.X_test_scaled = X_test_scaled

        self.model_initializer()

    def grid_search(self, model):
    
        grid = GridSearchCV(self.models[model], settings.PARAMETER_SEARCH[model], scoring=settings.PARAMETER_SCORING, cv=settings.PARAMETER_CV, n_jobs=-1)
        if model in ['RandomForest', 'XGBoost']:
            grid.fit(self.X_train, self.y_train)
        elif model in ['LSTM']:
            grid.fit(torch.tensor(self.X_train_scaled).float(), torch.tensor(self.y_train.values).float()) 
        else: 
            grid.fit(self.X_train_scaled, self.y_train)

        self.results[model] = {
            'best_params': grid.best_params_,
            'best_score': grid.best_score_
        }

        if model in ['RandomForest', 'XGBoost']:
            self.predictions[model] = grid.best_estimator_.predict(self.X_test)
        elif model in ['LSTM']:
            self.predictions[model] = grid.best_estimator_.predict(torch.tensor(self.X_test_scaled).float())
        else:
            self.predictions[model] = grid.best_estimator_.predict(self.X_test_scaled)
        
        return 
    
    def model_initializer(self):
            
        self.models['LinearRegression'] = LinearRegression()
        self.models['RandomForest'] = RandomForestRegressor(random_state=42)
        self.models['XGBoost'] = XGBRegressor(random_state=42, verbosity=0)
        self.models['MLPRegressor'] = MLPRegressor(random_state=42, max_iter=500) # Ensure X_train has the shape (samples, timesteps, features)
        lstm_model = create_lstm_model(self.X_train_scaled.shape[1] )
        self.models['LSTM'] = lstm_model

    def save_predictions(self, predictions):
        
        if not os.path.exists(os.path.join(settings.RESULTS_FOLDER_PATH,'predictions')):
            os.makedirs(os.path.join(settings.RESULTS_FOLDER_PATH,'predictions'))

        predictions.to_csv(os.path.join(settings.RESULTS_FOLDER_PATH,'predictions',f"{self.target}.csv"), index=False)
        
        return
    
    def data_to_csv(self):

        predictions_df = pd.DataFrame()

        for key in self.predictions: 
            temp_predictions = self.predictions[key]
            columns = [col + f"_{key}" for col in settings.TARGETS_FOR_ML_MODEL[self.target]]
            temp_df = pd.DataFrame(temp_predictions, columns=columns, index=self.y_test.index)
            predictions_df = pd.concat([predictions_df, temp_df], axis=1)

        self.save_predictions(predictions_df)

        return


    def run(self, target):

        self.target = target
        print('----------------------------------------------------------------')
        print(f'Started hyperparameter for parametar: {target}')
        print('----------------------------------------------------------------')
        for model in settings.MODELS:
            print(f"Processing model: {model}")
            self.grid_search(model)
            print(f"Model {model} done.")
        self.data_to_csv()

        return self.results






