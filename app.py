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

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            # Collecting data from the form
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Convert data to DataFrame
            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:", pred_df)

            # Prediction pipeline
            predict_pipeline = PredictPipeline()
            print("Starting Prediction...")
            results = predict_pipeline.predict(pred_df)
            print("Prediction Completed. Results:", results)

            # Render the results
            return render_template('home.html', results=results[0])

    except Exception as e:
        # Log the error and return an error message
        print("Error occurred:", e)
        return render_template('home.html', error="An error occurred during prediction. Please try again.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)