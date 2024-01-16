import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:                                          # a Class which only stores data paths
    train_data_path:str = os.path.join("artifacts","train.csv")   # string return type;    # returns 'artifacts\train.csv'
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()       # Initialise 'DataIngestionConfig' class: has three data path variables


    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion component")    # Logging the step
        try:
            df = pd.read_csv('notebook\data\stud.csv')      # Reading data
            logging.info("Read the dataset as dataframe")       # Logging the step

            # Create the Directory where data will be stored:
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)   # extract parent folder name and create a folder with the name

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)   # save the raw data to our designated location

            logging.info("Train-Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)          # Train-Test Split
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)   # save the train data to our designated location
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)     # save the test data to our designated location

            logging.info("Data ingestion is completed")

            return (
                self.ingestion_config.train_data_path,       # returning train test data paths, will be required in the data transformation step later
                self.ingestion_config.test_data_path
            )

        except Exception as e:                  # raise Custom Exception if above code face error
            raise CustomException(e, sys)
            



if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()




