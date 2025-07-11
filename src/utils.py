import yaml
import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, RandomOverSampler,ADASYN
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def load_config(config_path='config/config.yaml'):
    """Load configuration from a YAML file.
    Args:
        config_path (str): Path to the configuration file.
    returns:
        dict: Configuration dictionary.
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        raise

    def save_model(model, model_path):
        """Save the trained model to a file.
        Args:
            model: The trained model to save.
            model_path (str): Path where the model will be saved. 
        """
        try:
            if hasattr(model, 'save_model')