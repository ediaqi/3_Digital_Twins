import json
import os
import pickle
import re

import settings 

def sanitize_filename(filename):
    """Sanitizes the filename by replacing special characters with underscores."""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', filename)

def data_split(X, y, train_size=settings.TRAIN_SIZE): 

    train_size = int(len(X) * train_size)
    X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
    y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

    return X_train, X_test, y_train, y_test

def save_scaler(scaler, target):

    if not os.path.exists(os.path.join(settings.RESULTS_FOLDER_PATH,'scalers')):
        os.makedirs(os.path.join(settings.RESULTS_FOLDER_PATH,'scalers'))
    target_name = sanitize_filename(target)

    with open(os.path.join(settings.RESULTS_FOLDER_PATH,'scalers', f'{target_name}_scaler.pkl'), "wb") as f:
        pickle.dump(scaler, f)

def save_results(results, target):

    if not os.path.exists(os.path.join(settings.RESULTS_FOLDER_PATH,'hyperparameters')):
        os.makedirs(os.path.join(settings.RESULTS_FOLDER_PATH,'hyperparameters'))

    target_name = sanitize_filename(target)

    with open(os.path.join(settings.RESULTS_FOLDER_PATH, 'hyperparameters', f"{target_name}_hyperparameters.json"), "w") as json_file:
        json.dump(results, json_file, indent=4)

    return
