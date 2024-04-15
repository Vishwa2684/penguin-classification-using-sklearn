# API for my python model
import pickle
from flask import Flask

app=Flask(__name__)

@app.route('/')
def start():
    return '<h1>Backend for my model</h1>'

if __name__=='__main__':
    app.run(port=8080,debug=True)