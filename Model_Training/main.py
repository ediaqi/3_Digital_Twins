from sklearn.preprocessing import StandardScaler

import settings
from training.utils import Hyperparameter_optimization
from preprocessing.main import DataPreprocessing
from training.prophet_model import prophet_results
from utils import save_results, data_split, save_scaler

data = DataPreprocessing()
data = data.return_dataset()

for target in settings.TARGETS_FOR_ML_MODEL:
    print('----------------------------------------------------------------')
    print(f'Started training for parametar: {target}')
    print('----------------------------------------------------------------')
    y = data[settings.TARGETS_FOR_ML_MODEL[target]]
    X = data.drop(columns=settings.TARGETS_FOR_ML_MODEL[target], axis=0)
    if target == 'PM10':
        X = X.drop(columns=settings.TARGETS_FOR_ML_MODEL['PM25'], axis=0)
    
    if target == 'PM25':
        X = X.drop(columns=settings.TARGETS_FOR_ML_MODEL['PM10'], axis=0)

    X_train, X_test, y_train, y_test = data_split(X, y)
    prophet_results(y_train, y_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    save_scaler(scaler, target)

    hyperparameter_optimization = Hyperparameter_optimization(X_train, X_train_scaled, y_train, X_test, X_test_scaled, y_test)
    results = hyperparameter_optimization.run(target)

    save_results(results, target)

    for model, result in results.items():
        print(f"Model: {model}")
        print(f"Best Params: {result['best_params']}")
        print(f"Best Score: {result['best_score']:.4f}")
        print()
