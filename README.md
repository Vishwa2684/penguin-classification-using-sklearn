# sklearn model to classify penguins based on flipper length,culmen length,culmen depth,body mass ,gender and island
- i did this project to understand how to link frontend with our ML model
- I'm interested in doing further projects related to AI/ML
- I used sklearn to create the ML model
- If u guys have better ways to filter and clean the data or improve something in the model just drop them in issues

# How to use the model in flask server
- to use the model in flask server u have to activate ur virtual environment using
   `venv\Scripts\activate`
- then run the model.py file once in ormal terminal or cmd
- after running the model.py, run flask server
- After, running the flask server go to client and type
   `npm install`
   `npm start`
    to run the frontend
- Then fill out the fields in the form and click on 'Predict' button to make a POST request to flask server where the model is unpickled
- and get the prediction of the values you've filled in the form
