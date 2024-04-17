# API for my python model
import pickle
import numpy as np
from flask import Flask,request,jsonify
from flask_cors import CORS
import requests

model = pickle.load(open('./model.pkl'))

app=Flask(__name__)
CORS(app)
@app.route('/')
def start():
    return '<h1>Backend for my model</h1>'

@app.route('/data')
def data():
    return {"data":['Apple','Banana','Pineapple']}

@app.route('/model')
def model():
    try:
        data = request.json
    
        # Extract the relevant features from the data
        input_data = [data[key] for key in ['Island', 'Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)', 'Sex']]
    
        # Make predictions
        predictions = model.predict([input_data])
    
        # Return the predictions as JSON
        return jsonify({'predictions': predictions.tolist()})
    except:
        return {"error":"bad request"}

    

if __name__=='__main__':
    app.run(port=8080,debug=True)