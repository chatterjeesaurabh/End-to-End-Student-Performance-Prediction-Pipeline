import os
import sys

import numpy as np
import pandas as pd
import dill                # helps saving the any object in a location
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV       # for using different hyperparameters on each models

from src.exception import CustomException


# To Save an object 'obj' to location with file name defined in 'file_path':
def save_object(file_path, obj):       
    try:
        dir_path = os.path.dirname(file_path)       # parent folder name

        os.makedirs(dir_path, exist_ok=True)        # create the folder

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)                # save the object into the folder
    
    except Exception as e:
        raise CustomException(e,sys)


# To Train model on train dataset, then evaluate model performance (R2-Score) in test dataset:
def evaluate_models(X_train, y_train, X_test, y_test, models, params):      
    try:
        report = {}         # Dictionary of all model's R2-score performance

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]       # parameters for grid-search of hyper-parameters

            gs = GridSearchCV(model, para, cv=3)        # 'Grid Search Cross-Validation' object prepared
            gs.fit(X_train, y_train)                    # performing grid-search of hyper-parameters on all models

            model.set_params(**gs.best_params_)         # set model parameters to the best ones obtained from the Grid search

            model.fit(X_train, y_train) # Train model

            # Make predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            # Evaluate Train and Test dataset
            train_model_score = r2_score(y_train, y_train_pred)     # R2-score on Train data
            test_model_score = r2_score(y_test, y_test_pred)        # R2-score on Test data

            report[list(models.keys())[i]] = test_model_score
        
        return report
    
    except Exception as e:
        raise CustomException(e,sys)



# To load 'PKL' or any file:
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)

