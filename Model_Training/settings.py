
DATA_PATH = 'data/df.csv'
OUTLIERS_WINDOW = 3
OUTLIERS_QUANTILE_LOW = 0.25
OUTLIERS_QUANTILE_HIGH = 0.75
LAGS_CREATING = 1

LAG_COLUMNS = ['CO2_device_316', 'TVOC_device_316',
        'CO_device_316', 'PM1_device_316',
        'PM25_device_316', 'PM10_device_316', 'temperature_device_316',
        'humidity_device_316', 'atmospheric_pressure_device_316',
        'CO2_device_4', 'TVOC_device_4', 'CO_device_4', 'PM1_device_4',
        'PM25_device_4', 'PM10_device_4', 'temperature_device_4',
        'humidity_device_4', 'atmospheric_pressure_device_4', 'CO2_device_7',
        'TVOC_device_7', 'CO_device_7', 'PM1_device_7', 'PM25_device_7',
        'PM10_device_7', 'temperature_device_7', 'humidity_device_7',
        'atmospheric_pressure_device_7', 'CO2_device_13', 'TVOC_device_13',
        'CO_device_13', 'PM1_device_13', 'PM25_device_13', 'PM10_device_13',
        'temperature_device_13', 'humidity_device_13',
        'atmospheric_pressure_device_13', 'NetCO2-CO2(ppm)_LS0623020168',
        'NetADC_O3-O3(ppb)_LS0623020168', 'NetADC_CO-CO( ppb)_LS0623020168',
        'NetPM-PM10(µg/m3)_LS0623020168', 'NetPM-PM25(µg/m3)_LS0623020168',
        'NetPid_P1-PPB(ppm)_LS0623020168', 'NetBME280-PERC(%)_LS0623020168',
        'NetBME280-TEMP_EXT(°C)_LS0623020168',
        'NetBME280-HPA(hPa)_LS0623020168', 'NetADC_NO2-NO2(ppb)_LS0623020168',
        'NetCO2-CO2(ppm)_LS0623020169', 'NetADC_O3-O3(ppb)_LS0623020169',
        'NetADC_CO-CO( ppb)_LS0623020169', 'NetPM-PM10(µg/m3)_LS0623020169','NetPM-PM25(µg/m3)_LS0623020169', 'NetPid_P1-PPB(ppm)_LS0623020169',
        'NetBME280-PERC(%)_LS0623020169', 'NetBME280-TEMP_EXT(°C)_LS0623020169',
        'NetBME280-HPA(hPa)_LS0623020169', 'NetADC_NO2-NO2(ppb)_LS0623020169',
        'NO2_device_402', 'O3_device_402', 'SO2_device_402', 'CO_device_402',
        'PM1_device_402', 'PM25_device_402', 'PM10_device_402', 'NO_device_402',
        'CO2_device_402', 'temperature_device_402', 'humidity_device_402',
        'atmospheric_pressure_device_402', 'noise_device_402']

PARAMETER_SEARCH = {
    'LinearRegression':{
        'fit_intercept': [True, False],
    },
    'RandomForest' : {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    },
    'XGBoost': {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0]
    },
    'MLPRegressor' : {
        'hidden_layer_sizes': [(50,), (100,), (50, 50)],
        'activation': ['relu', 'tanh'],
        'solver': ['adam', 'sgd'],
        'alpha': [0.0001, 0.001, 0.01],
        'learning_rate': ['constant', 'adaptive']
    },
    'LSTM' : {
        'module__hidden_dim': [50, 100],
        'module__num_layers': [1, 2],
        'lr': [0.01, 0.001],
        'batch_size': [16, 32],
        'max_epochs': [10, 20]
    }
}

PARAMETER_SCORING = 'neg_mean_squared_error'
PARAMETER_CV = 5 

MODELS = ['LinearRegression', 'RandomForest', 'XGBoost', 'MLPRegressor', 'LSTM']

RESULTS_FOLDER_PATH = './results'

TARGETS_FOR_ML_MODEL = {
    'CO2':['CO2_device_316', 'CO2_device_4', 'CO2_device_7', 'CO2_device_13', 'NetCO2-CO2(ppm)_LS0623020168', 'NetCO2-CO2(ppm)_LS0623020169'],
    'CO':['CO_device_316', 'CO_device_4', 'CO_device_7', 'CO_device_13', 'NetADC_CO-CO( ppb)_LS0623020168', 'NetADC_CO-CO( ppb)_LS0623020169'],
    'TVOC':['TVOC_device_316', 'TVOC_device_4', 'TVOC_device_7', 'TVOC_device_13', 'NetPid_P1-PPB(ppm)_LS0623020168', 'NetPid_P1-PPB(ppm)_LS0623020169'],
    'PM25':['PM25_device_316', 'PM25_device_4', 'PM25_device_7', 'PM25_device_13', 'NetPM-PM25(µg/m3)_LS0623020168', 'NetPM-PM25(µg/m3)_LS0623020169'],
    'PM10':	['PM10_device_316', 'PM10_device_4', 'PM10_device_7', 'PM10_device_13', 'NetPM-PM10(µg/m3)_LS0623020168', 'NetPM-PM10(µg/m3)_LS0623020169'],
    'temperature':['temperature_device_316', 'temperature_device_4', 'temperature_device_7', 'temperature_device_13', 'NetBME280-TEMP_EXT(°C)_LS0623020168', 'NetBME280-TEMP_EXT(°C)_LS0623020169'],
    'humidity':['humidity_device_316', 'humidity_device_4', 'humidity_device_7', 'humidity_device_13', 'NetBME280-PERC(%)_LS0623020168', 'NetBME280-PERC(%)_LS0623020169'],
    'atmospheric_pressure':['atmospheric_pressure_device_316', 'atmospheric_pressure_device_4', 'atmospheric_pressure_device_7', 'atmospheric_pressure_device_13', 'NetBME280-HPA(hPa)_LS0623020168', 'NetBME280-HPA(hPa)_LS0623020169'],
}
TRAIN_SIZE = 0.80
