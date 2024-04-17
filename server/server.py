# API for my python model
import pickle
from flask import Flask,request,jsonify
from flask_cors import CORS
import requests

with open('../model.pkl') as file:
    model = pickle.load(file)

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
    form_data=request.json
    culmen_length=form_data['culmenLength']
    culmen_depth=form_data['culmenDepth']

    

if __name__=='__main__':
    app.run(port=8080,debug=True)