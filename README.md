# AI-Powered EV Driving Efficiency Optimizer

## Overview

The AI-Powered EV Driving Efficiency Optimizer is a Machine Learning-based application that analyzes driving behavior and predicts electric vehicle energy consumption. The system provides intelligent recommendations to improve driving efficiency and maximize EV battery range.

## Features

* Predicts EV energy consumption using Machine Learning
* Analyzes driving parameters such as speed, terrain, braking, and acceleration
* Provides AI-based driving recommendations
* Uses Random Forest Regression for prediction
* Interactive command-line interface

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Machine Learning
* Random Forest Regression

## Project Structure

AI-EV-Efficiency-Optimizer/

data/

* driving_data.csv

models/

* ev_model.pkl

src/

* train_model.py
* predictor.py
* driving_tips.py

## How to Run

1. Create a virtual environment:
   python -m venv venv

2. Activate the environment:
   Windows:
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the training script:
   cd src
   python train_model.py

5. Run the predictor:
   python predictor.py

## Future Improvements

* Web dashboard using Streamlit
* Real-time EV sensor integration
* Larger datasets for better prediction accuracy
* Advanced Deep Learning models

## Author

Ishika Sarkar
