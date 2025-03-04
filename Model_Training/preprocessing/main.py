import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer

import settings


class DataPreprocessing:

    def __init__(self):

        self.df = pd.read_csv(settings.DATA_PATH, index_col=0)
        print('Data Processing Started')
        print('----------------------------------------------------------------')
        print('Removing outliers...')
        self.df = self.remove_outliers()
        print('Encoding time')
        self.encode_time_as_sinusoidal()
        print('Removing NaNs...')
        self.remove_nans()
        print('Creating lag features...')
        self.df = self.create_lag_features()
        print('Data Processing Done')

    def remove_outliers(self, window=settings.OUTLIERS_WINDOW):
        cleaned_data = self.df.copy()

        for column in self.df.columns:
            rolling_window = self.df[column].rolling(window=window, min_periods=1)
            Q1 = rolling_window.quantile(settings.OUTLIERS_QUANTILE_LOW)
            Q3 = rolling_window.quantile(settings.OUTLIERS_QUANTILE_HIGH)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            cleaned_data[column] = self.df[column].where(
                (self.df[column] >= lower_bound) & (self.df[column] <= upper_bound), np.nan
            )

        return cleaned_data

    def remove_nans(self):
        simple_imputer = SimpleImputer(strategy='mean')
        self.df = pd.DataFrame(simple_imputer.fit_transform(self.df), columns=self.df.columns, index=self.df.index)
        imputer = IterativeImputer()
        numeric_cols = self.df.select_dtypes(include=["number"]).columns
        cols_to_impute = self.df[numeric_cols].columns[self.df[numeric_cols].isna().any()]
        
        if cols_to_impute.empty:
            print("No columns to impute, skipping imputation.")
            return

        df_to_impute = self.df[cols_to_impute]
        df_imputed = imputer.fit_transform(df_to_impute)

        self.df[cols_to_impute] = pd.DataFrame(
            df_imputed, columns=cols_to_impute, index=self.df.index
        )

    def create_lag_features(self, lags=settings.LAGS_CREATING, method="mode"):
        df_with_lags = self.df.copy()
        for column in settings.LAG_COLUMNS:
            for lag in range(1, lags + 1):
                if method == "mode":
                    df_with_lags[f"{column}_lag_{lag}_mode"] = (
                        self.df[column]
                        .rolling(window=lag, min_periods=1)
                        .apply(lambda x: pd.Series(x).mode().iloc[0] if not pd.Series(x).mode().empty else x.mean(), raw=False)
                    )
                elif method == "mean":
                    df_with_lags[f"{column}_lag_{lag}_mean"] = self.df[column].rolling(window=lag, min_periods=1).mean()
                else:
                    raise ValueError("Invalid method. Use 'mode' or 'mean'.")
        return df_with_lags

    def encode_time_as_sinusoidal(self):
        temp_df = pd.DataFrame()

        temp_df.index = pd.to_datetime(self.df.index)
        temp_df['weekday'] = temp_df.index.weekday
        if not pd.api.types.is_datetime64_any_dtype(self.df.index):
            self.df.index = pd.to_datetime(self.df.index)

        temp_df['day_fraction'] = (temp_df.index.hour * 60 + self.df.index.minute) / (24 * 60)
        temp_df['day_sin'] = np.sin(2 * np.pi * temp_df['weekday'] / 7)
        temp_df['hour_sin'] = np.sin(2 * np.pi * temp_df['day_fraction'])

        self.df = pd.concat([self.df, temp_df[['day_sin', 'hour_sin']]], axis=1)
        return
    
    def return_dataset(self):
        return self.df
    