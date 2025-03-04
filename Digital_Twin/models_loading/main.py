import logging
import joblib
import os
import pickle

from pathlib import Path

import settings
import utility.s3 as s3_utils
from utility.common import format_logger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
format_logger(logger)

class ModelLoader():

    MODEL_DIR = Path(__file__).parent / 'models'

    def __init__(self):

        self.models_filtration = {}
        self.models_no_filtration = {}

        self.scalers_filtration = {}
        self.scalers_no_filtration = {}

        self._check_if_downloaded('s3://ascalia-deploy/ediaqi-digital-twin/', download_dir_path=self.MODEL_DIR)
        self.prepare_models()

    def _check_if_downloaded(self, object_path: str, download_dir_path: str) -> Path:
        """
        Checks if file/directory object_path exists. If it does, the function does nothing (returns the specified path).

        If the file/directory does not exists and it is a S3 uri, the function downloads the files to the specified
        directory and returns the path of the downloaded object.

        @param object_path: path to the object where it should be
        @param download_dir_path: if the object does not exist at the specified path, download it to
        download_dir_path/object_path

        @return: path of the existing/downloaded object, Path
        """
        download_path = Path(download_dir_path) / object_path.split("/")[-1]

        if download_path.exists() and any(download_path.iterdir()):
            logger.info(f"Found file {download_path}.")
            return download_path

        if object_path.startswith("s3://"):
            logger.info(f"Downloading files from {object_path} to {download_dir_path}")
            s3_utils.download_dir(s3_uri=object_path, output_path=download_dir_path)
            logger.info(f"Done.")
            return download_path
        else:
            logger.error(f"File {object_path} does not exist!")
            return Path(object_path)

    @staticmethod
    def load_models(path, dict_for_data):
        """
        Load machine learning models from the specified directory and store them in the provided dictionary.

        Args:
            path (str): The directory path where the model files are located.
            dict_for_data (dict): A dictionary to store the loaded models, with targets as keys.

        Returns:
            dict: The updated dictionary containing the loaded models.

        Raises:
            FileNotFoundError: If a model file is not found at the specified path.
            Exception: For any other exceptions that occur during model loading.

        Example:
            models_dict = {}
            models_dict = load_models('/path/to/models', models_dict)
        """
        logger.info(f"Loading models")
        for target in settings.TARGETS_FOR_ML_MODELS:
            path_model = os.path.join(path, f"{target}_LinearRegression.pkl")
            dict_for_data[target] = joblib.load(path_model)
        logger.info(f"Models loaded")
        return dict_for_data
    
    @staticmethod
    def load_scalers(path, dict_for_data):
        """
        Load scalers from the specified path and update the provided dictionary with the scalers.

        Args:
            path (str): The directory path where the scaler files are located.
            dict_for_data (dict): The dictionary to be updated with the loaded scalers.

        Returns:
            dict: The updated dictionary containing the loaded scalers.

        Raises:
            FileNotFoundError: If any of the scaler files are not found in the specified path.
            pickle.UnpicklingError: If there is an error unpickling the scaler files.
        """
        logger.info(f"Loading scalers")
        for target in settings.TARGETS_FOR_ML_MODELS:
            path_scaler = os.path.join(path, f"{target}_scaler.pkl")
            dict_for_data[target] = pickle.load(open(path_scaler, 'rb'))
        logger.info(f"Scalers loaded")
        return dict_for_data

    def prepare_models(self):

        self.models_filtration = self.load_models(settings.MODELS_PATH_FILTRATION, self.models_filtration)
        self.models_no_filtration = self.load_models(settings.MODELS_PATH_NO_FILTRATION, self.models_no_filtration)
        
        self.scalers_filtration = self.load_scalers(settings.SCALERS_PATH_FILTRATION, self.scalers_filtration)
        self.scalers_no_filtration = self.load_scalers(settings.SCALERS_PATH_NO_FILTRATION, self.scalers_no_filtration)
