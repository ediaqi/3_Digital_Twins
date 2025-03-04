import logging

import numpy as np
import pandas as pd
import pytz
from datetime import datetime, timedelta

import settings
from models_loading.main import ModelLoader
from utility.common import format_logger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
format_logger(logger)

class DataProcessor(ModelLoader):

    def __init__(self):

        super().__init__()

        self.data = None
        self.timestamp = None
        self.data_for_model = {}
        self.filtering_unit_on = {}
        self.filtering_unit_off = {}
        self.results = {}

    def get_time(self):
        """
            Get the current time in the 'Europe/Zagreb' timezone and format it as a timestamp.
            This method retrieves the current UTC time and adjusts it based on the following rules:
            - If the current second is greater than or equal to 25, the time is rounded up to the next minute.
            - Otherwise, the seconds and microseconds are set to zero.
            The adjusted time is then converted to the 'Europe/Zagreb' timezone and formatted as a string
            in the format "YYYY-MM-DD HH:MM:SS".
            The formatted timestamp is stored in the `self.timestamp` attribute.
        """
        utc_now = datetime.now(pytz.utc)
        if utc_now.second >= 25:
            utc_now = utc_now.replace(second=0, microsecond=0) + timedelta(minutes=1)
        else:
            utc_now = utc_now.replace(second=0, microsecond=0)

        zagreb_tz = pytz.timezone(settings.TIMEZONE)
        zagreb_time = utc_now.astimezone(zagreb_tz)
        self.timestamp = zagreb_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_sensor_features(self):
        """
        Extracts and processes sensor features for both indoor and outdoor environments.
        This method performs the following steps:
        1. Calls the `get_time` method to set the current timestamp.
        2. Initializes the `data_for_model` dictionary with the current timestamp.
        3. Iterates over the `INDOOR_ENVIRONMENT_FEATURES` from the settings and updates the `data_for_model` dictionary with the corresponding values from the indoor environment data.
        4. Iterates over the `OUTDOOR_ENVIROMENT_FEATURES` from the settings and updates the `data_for_model` dictionary with the corresponding values from the outdoor environment data.
        The method handles special cases for 'CO_values' by setting a default value of 0.5.
        Attributes:
            self.timestamp (datetime): The current timestamp.
            self.data (dict): The data containing sensor readings for indoor and outdoor environments.
            self.data_for_model (dict): The dictionary to store processed sensor features for the model.
        """

        self.get_time()
        self.data_for_model = {'timestamp': self.timestamp}

        for item, params in settings.INDOOR_ENVIRONMENT_FEATURES.items():
            value = 0.5 if item == 'CO_values' else self.data["indoor"][settings.CONNECTING_INPUTS_INDOOR[item]]
            self.data_for_model.update({param: value if 'CO_' in param else self.data["indoor"][settings.CONNECTING_INPUTS_INDOOR[item]] for param in params})

        for item, params in settings.OUTDOOR_ENVIROMENT_FEATURES.items():
            self.data_for_model.update({param: value if 'CO_' in param else self.data["outdoor"][settings.CONNECTING_INPUTS_OUTDOOR[item]] for param in params})

    def add_traffic_features(self):
        """
        Adds traffic-related features to the model data based on the number of different types of vehicles.
        This method processes the number of cars, trucks, buses, and motorcycles from the 'Additional information' 
        section of the data and updates the model data with dummy variables representing the presence of these vehicles.
        The number of dummy variables created for each vehicle type is determined by the settings.MAX_DUMMIES_FOR_TRAFFIC 
        configuration. If the count of a vehicle type exceeds the maximum allowed dummies, the last dummy variable is set 
        to 1, indicating the overflow.
        The updated model data is stored in the `self.data_for_model` attribute.
        Attributes:
            self.data (dict): The input data containing 'Additional information' with vehicle counts.
            self.data_for_model (dict): The dictionary to be updated with traffic-related dummy variables.
        Example:
            If the input data contains:
            self.data = {
                "Additional information": {
                    "Number of cars": 3,
                    "Number of trucks": 1,
                    "Number of buses": 0,
                    "Number of motorcycles": 2
            and settings.MAX_DUMMIES_FOR_TRAFFIC = {"car": 3, "truck": 2, "bus": 1, "motorcycle": 2},
            the `self.data_for_model` will be updated with:
            {
                "car_0": 1,
                "car_1": 1,
                "car_2": 1,
                "car_3": 0,
                "truck_0": 1,
                "truck_1": 0,
                "bus_0": 0,
                "motorcycle_0": 1,
                "motorcycle_1": 1,
                "motorcycle_2": 0
        """
        user_input = {
                        'car': self.data["additionalInfo"]['cars'],
                        'truck': self.data["additionalInfo"]['trucks'],
                        'bus': self.data["additionalInfo"]['buses'],
                        'motorcycle': self.data["additionalInfo"]['motorcycles'],
                    }

        for vehicle, count in user_input.items():
            category = vehicle.split()[-1].lower() 
            max_columns = settings.MAX_DUMMIES_FOR_TRAFFIC[category] + 1
            
            if count > max_columns:
                self.data_for_model.update({f"{category}_{i}": 1 if i == max_columns - 1 else 0 for i in range(max_columns)})
            else:
                self.data_for_model.update({f"{category}_{i}": 1 if i < count else 0 for i in range(max_columns)})

    def add_window_feature(self):
        """
        Adds a new feature 'Small_window' to the data_for_model dictionary based on the 
        'Ventilation' -> 'Window' status in the data dictionary. If the window status is 'On', 
        'Small_window' is set to 1, otherwise it is set to 0.
        
        Returns:
            None
        """
        window_status = bool(self.data["ventilation"]["window"])
        self.data_for_model['Small_window'] = 1 if window_status == True else 0

    def convert_dict_to_dataframe(self):
        self.data_for_model = pd.DataFrame(self.data_for_model, index=[self.data_for_model['timestamp']])

    def calculate_Ct(C0, C_ext, n, t):
        """
        Calculate the concentration of a substance at time t.

        Parameters:
        C0 (float): Initial concentration of the substance.
        C_ext (float): External concentration of the substance.
        n (float): Rate constant.
        t (float): Time at which the concentration is calculated.

        Returns:
        float: The concentration of the substance at time t.
        """
        return C_ext + (C0 - C_ext) * np.exp(-n * t)

    def gas_tracing_features(self):
        """
        Generates gas tracing features for CO2 data.
        This method processes CO2 data by calculating new features based on elapsed times
        and the difference between CO2 measurements from different devices. The new features
        are added to the original dataset.
        Steps:
        1. Filters the CO2 data from the dataset.
        2. Defines the elapsed times for which new features will be calculated.
        3. For each CO2 column (except 'CO2_device_402'), calculates new features based on the 
            exponential decay formula and the elapsed times.
        4. Drops the original CO2 columns from the dataset.
        5. Concatenates the new CO2 features with the original dataset.
        Note:
        - The exponential decay formula used is: 
          CO2_data['CO2_device_402'] + (CO2_data[column] - CO2_data['CO2_device_402']) * np.exp(-settings.CO2_N_VALUES[column] / 60 * elapsed)
        - The settings.CO2_N_VALUES dictionary should contain the necessary decay values for each CO2 column.
        Attributes:
        - self.data_for_model (pd.DataFrame): The dataset containing the CO2 data and other features.
        Returns:
        - None: The method updates the self.data_for_model attribute in place.
        """
        CO2_data = self.data_for_model.filter(like='CO2', axis=1)
        columns_to_drop_later = CO2_data.columns

        elapsed_times = [1, 5, 10]

        for column in CO2_data.columns:
            if column != 'CO2_device_402':
                for elapsed in elapsed_times:
                    CO2_data.loc[:, f'{column}_{elapsed}'] = CO2_data['CO2_device_402'] + (CO2_data[column] - CO2_data['CO2_device_402']) * np.exp(-settings.CO2_N_VALUES[column] / 60 * elapsed)

        CO2_data = CO2_data.drop(columns = columns_to_drop_later)
        self.data_for_model = pd.concat([self.data_for_model, CO2_data], axis=1)

    @staticmethod
    def euclidean_distance(sensor_pos, filter_pos):
        return np.sqrt(sum((np.array(sensor_pos) - np.array(filter_pos))**2))

    def filtering_unit_features(self):
        """
        Calculates the influence of the filtering unit on each sensor based on their positions.
        This method computes the influence of the filtering unit on each sensor by calculating the inverse of the 
        Euclidean distance between the sensor and the filtering unit position. The results are stored in two 
        DataFrames: one for when the filtering unit is on and one for when it is off.
        The filtering unit positions are taken from the 'Position of filtering unit' columns in the data attribute.
        The sensor positions are taken from the SENSOR_PLACEMENT dictionary in the settings module.
        The feature names are renamed using the RENAMING_FEATURES_FILTERING_UNIT dictionary in the settings module.
        The resulting DataFrames are stored in the filtering_unit_on and filtering_unit_off attributes.
        Returns:
            None
        """
        filtering_unit_possition = [self.data["filteringUnit"]["x"],
                                    self.data["filteringUnit"]["y"],
                                    self.data["filteringUnit"]["z"]]
        
        self.filtering_unit_on = {settings.RENAMING_FEATURES_FILTERING_UNIT[sensor]:round(1 / self.euclidean_distance(pos, filtering_unit_possition),5) for sensor, pos in settings.SENSOR_PLACEMENT.items()}
        self.filtering_unit_off = {key: 0 for key in self.filtering_unit_on}

        self.filtering_unit_on = pd.DataFrame(self.filtering_unit_on, index = self.data_for_model.index)
        self.filtering_unit_off = pd.DataFrame(self.filtering_unit_off, index = self.data_for_model.index)

        self.filtering_unit_on.index = pd.to_datetime(self.filtering_unit_on.index)
        self.filtering_unit_off.index = pd.to_datetime(self.filtering_unit_off.index)

    def mass_balance_features(self):
        """
        Calculate mass balance features for the model data.
        This method processes the data for the model by calculating the mass balance
        features for each indoor column specified in the settings.INDOOR_COL_FOR_MASS_BALANCE.
        It creates new features based on the mass balance equations and appends them to the
        existing data.
        The method performs the following steps:
        1. Converts the index of the data_for_model DataFrame to datetime.
        2. Iterates over each indoor column specified in settings.INDOOR_COL_FOR_MASS_BALANCE.
        3. Creates a temporary DataFrame with the indoor column, corresponding outdoor column,
            and the 'Small_window' column.
        4. Calculates the derivative of the indoor column with respect to time (dI/dt).
        5. Applies the mass balance equation to calculate the new feature (S) based on the
            presence of a small window.
        6. Drops any rows with missing values in the temporary DataFrame.
        7. Concatenates the new features (dI/dt and S) to the original data_for_model DataFrame.
        The mass balance equation used is:
        - If 'Small_window' is 1:
            S = dI/dt - P_LAMBDA * O + (LAMBDA + LAMBDAD) * I
        - Otherwise:
            S = dI/dt + (LAMBDA + LAMBDAD) * I
        The method relies on the following settings:
        - settings.INDOOR_COL_FOR_MASS_BALANCE: List of indoor columns to process.
        - settings.INDOOR_OUTDOOR_CONNECTION_MASS_BALANCE: Mapping of indoor columns to corresponding outdoor columns.
        - settings.P_LAMBDA_MASS_BALANCE: Dictionary of P_LAMBDA values for each indoor column.
        - settings.LAMBDA_MASS_BALANCE: Dictionary of LAMBDA values for each indoor column.
        - settings.LAMBDAD_MASS_BALANCE: Dictionary of LAMBDAD values for each indoor column.
        Returns:
            None
        """

        self.data_for_model.index = pd.to_datetime(self.data_for_model.index)

        for col_in in settings.INDOOR_COL_FOR_MASS_BALANCE:
            temp_df = pd.concat([self.data_for_model[col_in], self.data_for_model[settings.INDOOR_OUTDOOR_CONNECTION_MASS_BALANCE[col_in]], self.data_for_model['Small_window']], axis=1)
            temp_df.columns = ['I', 'O', 'Small_window']
            
            temp_df[f"{col_in}_dI/dt"] = temp_df["I"]
            temp_df[f"{col_in}_S"] = temp_df.apply(
                lambda row: (
                    row[f"{col_in}_dI/dt"] - settings.P_LAMBDA_MASS_BALANCE[col_in] * row["O"] +
                    (settings.LAMBDA_MASS_BALANCE[col_in] + settings.LAMBDAD_MASS_BALANCE[col_in]) * row["I"]
                ) if row['Small_window'] == 1 else (
                    row[f"{col_in}_dI/dt"] + (settings.LAMBDA_MASS_BALANCE[col_in] + settings.LAMBDAD_MASS_BALANCE[col_in]) * row["I"]
                ), axis=1
            )
            temp_df.dropna(inplace=True)
            self.data_for_model = pd.concat([self.data_for_model, temp_df[[f"{col_in}_dI/dt", f"{col_in}_S"]]], axis=1)

    def encoding_temporal_features(self):
        """
        Encodes temporal features from a timestamp into sinusoidal components.
        This method converts the timestamp into two sinusoidal features:
        - day_sin: Represents the day of the week as a sine wave.
        - hour_sin: Represents the fraction of the day as a sine wave.
        The resulting features are added to the `data_for_model` DataFrame.
        Returns:
            None
        """
        timestamp = pd.to_datetime(self.timestamp)
    
        weekday = timestamp.weekday()
        day_fraction = (timestamp.hour * 60 + timestamp.minute) / (24 * 60)
        
        day_sin = np.sin(2 * np.pi * weekday / 7)
        hour_sin = np.sin(2 * np.pi * day_fraction)

        temp_dict = {
            'day_sin': day_sin,
            'hour_sin': hour_sin
        }
        
        temp_df = pd.DataFrame(temp_dict, index = self.data_for_model.index)
        self.data_for_model = pd.concat([self.data_for_model, temp_df], axis=1)

    @staticmethod
    def create_lag_features(df, lags=1, method="mode"):
        df_with_lags = df.copy()
        for column in settings.LAG_FEATURES:
            for lag in range(1, lags + 1):
                if method == "mode":
                    df_with_lags[f"{column}_lag_{lag}_mode"] = (
                        df[column]
                        .rolling(window=lag, min_periods=1)
                        .apply(lambda x: pd.Series(x).mode().iloc[0] if not pd.Series(x).mode().empty else x.mean(), raw=False)
                    )
                elif method == "mean":
                    df_with_lags[f"{column}_lag_{lag}_mean"] = df[column].rolling(window=lag, min_periods=1).mean()
                else:
                    raise ValueError("Invalid method. Use 'mode' or 'mean'.")
        return df_with_lags

    def process_data(self):
        self.get_sensor_features()
        self.add_traffic_features()
        self.add_window_feature()
        self.convert_dict_to_dataframe()
        self.gas_tracing_features()
        self.filtering_unit_features()
        self.mass_balance_features()
        self.encoding_temporal_features()
        self.data_for_model = self.create_lag_features(self.data_for_model)

    def model_predictions(self):
        logger.info("Model predictions started.")
        for target in settings.TARGETS_FOR_ML_MODELS: 
            X_real_columns = [item for item in settings.COLUMNS_ORDER_FOR_MODEL if item not in settings.TARGETS_FOR_ML_MODELS[target]]
            X = self.data_for_model.drop(columns=settings.TARGETS_FOR_ML_MODELS[target], axis=0)

            if target == 'PM10':
                X = X.drop(columns=settings.TARGETS_FOR_ML_MODELS['PM25'], axis=0)
                X_real_columns = [item for item in X_real_columns if item not in settings.TARGETS_FOR_ML_MODELS['PM25']]
            
            if target == 'PM25':
                X = X.drop(columns=settings.TARGETS_FOR_ML_MODELS['PM10'], axis=0)
                X_real_columns = [item for item in X_real_columns if item not in settings.TARGETS_FOR_ML_MODELS['PM10']]

            X_no_filter = pd.concat([X, self.filtering_unit_off], axis=1)
            X_filter = pd.concat([X, self.filtering_unit_on], axis=1)

            X_no_filter = X_no_filter[X_real_columns]
            X_filter = X_filter[X_real_columns]

            X_no_filter = self.scalers_no_filtration[target].transform(X_no_filter)
            X_filter = self.scalers_filtration[target].transform(X_filter)

            y_filter = self.models_filtration[target].predict(X_filter)
            y_no_filter = self.models_no_filtration[target].predict(X_no_filter)
            self.results[target] = {'With_filter': round(y_filter[0][-1], 2), 'Without_filter': round(y_no_filter[0][-1],2)}
        logger.info("Model predictions finished.")
    def run(self, data):

        self.data = data
        logger.info("Data processing started.")
        self.process_data()
        logger.info("Data processing finished.")
        self.model_predictions()

        return self.results
    