import joblib
import os
import json
import pandas as pd

NUM_COLS = [
    'Distance_to_Shore', 'Turbidity', 'Cyclone_Frequency', 'Date_Month',
    'Date_Year', 'Depth_m', 'ClimSST', 'Temperature_Kelvin', 'Temperature_Mean',
    'Temperature_Maximum', 'Windspeed', 'SSTA', 'SSTA_DHW',
    'TSA', 'TSA_Maximum', 'TSA_Mean', 'TSA_Frequency',
    'TSA_DHW', 'TSA_DHWMax', 'TSA_DHWMean'
]
CAT_COLS = ['Realm_Name', 'Exposure']
ALL_COLS = NUM_COLS + CAT_COLS


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, 'rf_atlantic_model.pkl'))
    preprocessor = joblib.load(os.path.join(model_dir, 'rf_atlantic_preprocessor.pkl'))
    return model, preprocessor


def input_fn(request_body, content_type='application/json'):
    data = json.loads(request_body)
    return pd.DataFrame([data])[ALL_COLS]


def predict_fn(input_data, model):
    rf, preprocessor = model
    X = preprocessor.transform(input_data)
    prediction = rf.predict(X)[0]
    proba = rf.predict_proba(X)[0].tolist()
    return {'prediction': prediction, 'probability': proba}


def output_fn(prediction, accept='application/json'):
    return json.dumps(prediction), 'application/json'
