import pickle
import os

import pandas as pd
from prophet import Prophet

import settings

def prophet_results(y_train, y_test):

    os.makedirs(settings.RESULTS_FOLDER_PATH, exist_ok=True)
    print('----------------------------------------------------------------')
    print('Starting prophet model...')
    print('----------------------------------------------------------------')
    for col in y_train.columns:

        print(f"Processing column: {col}")

        y_train_col = y_train[col].reset_index()
        y_train_col = y_train_col.rename(columns={'timestamp': "ds", col: "y"})
        y_train_col["ds"] = pd.to_datetime(y_train_col["ds"])

        y_test_col = y_test[col].reset_index()
        y_test_col = y_test_col.rename(columns={'timestamp': "ds", col: "y"})
        y_test_col["ds"] = pd.to_datetime(y_test_col["ds"])

        model = Prophet(
                interval_width=0.95,
                growth="linear",
                seasonality_mode="multiplicative",
                yearly_seasonality=False,
                daily_seasonality=False,
                weekly_seasonality=False,
            )
        try:
            model.fit(y_train_col)
        except Exception as e:
            print(f"Error fitting model for {col}: {e}")
            continue

        future = model.make_future_dataframe(periods=len(y_test_col))
        forecast = model.predict(future)

        predictions = forecast.loc[forecast["ds"].isin(y_test_col["ds"]), ["ds", "yhat", "yhat_lower", "yhat_upper"]]
        merged = y_test_col.merge(predictions, on="ds")

        col_name = re.sub(r'[^a-zA-Z0-9_-]', '_', col)

        model_file = os.path.join(settings.RESULTS_FOLDER_PATH, f"prophet_model_{col_name}.pkl")
        forecast_file = os.path.join(settings.RESULTS_FOLDER_PATH, f"forecast_{col_name}.csv")            
        with open(model_file, 'wb') as f:
            pickle.dump(model, f)
            
        merged.to_csv(forecast_file, index=False)
        print(f"Saved results for {col}")
    
    print('End of prophet model...')
    
    return
