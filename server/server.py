# API for my python model
import pickle
import numpy as np
from flask import Flask,request,jsonify
from flask_cors import CORS
import requests
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



app=Flask(__name__)
CORS(app)
@app.route('/')
def start():
    return '<h1>Backend for my model</h1>'

@app.route('/model',methods=['POST'])
def model():
    try:
        model = pickle.load(open('./model.pkl','rb'))
        
        data = request.json
        species={
            1:'Adelie Penguin (Pygoscelis adeliae)',
            2:'Gentoo penguin (Pygoscelis papua)',
            3:'Chinstrap penguin (Pygoscelis antarctica)'
            }
        # Extract the relevant features from the data
        l=[]
        for i in data:
            l.append(int(data[i]))
        print(l)
        # Make predictions
        predictions = model.predict([l])
        print('Predictions',species[predictions[0]])
    
        # Return the predictions as JSON
        return jsonify({'predictions': species[predictions[0]]})
    except Exception as e:
        return {"error":e.args[0]}

    

if __name__=='__main__':
    app.run(port=8080,debug=True)