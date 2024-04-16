# API for my python model
import pickle
from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route('/')
def start():
    return '<h1>Backend for my model</h1>'

@app.route('/data')
def data():
    return {"data":['Apple','Banana','Pineapple']}

if __name__=='__main__':
    app.run(port=8080,debug=True)