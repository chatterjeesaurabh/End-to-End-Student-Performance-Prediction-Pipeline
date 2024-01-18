from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

app = application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])     # /predictdata is the main home page
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')       # home.html : page which has input fields to feed input data to predict
    
    else:
        data = CustomData(
            gender = request.form.get('gender'),      # accessing data from 'request' which has got all data from 'post' form in the html page
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('writing_score')),
            writing_score = float(request.form.get('reading_score'))
        )

        pred_df = data.get_data_as_data_frame()   # convert the data into DataFrame
        print(pred_df)

        predict_pipeline = PredictPipeline()            # load PredictPipeline object
        results = predict_pipeline.predict(pred_df)     # data prediction 

        return render_template('home.html', results=results[0])     # return to the home.html to show results there



# RUN the APP:
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)         # maps to "127.0.0.1:5000"


# Index Page:  127.0.0.1:5000

# Home Page (Predictor):  127.0.0.1:5000/predictdata



