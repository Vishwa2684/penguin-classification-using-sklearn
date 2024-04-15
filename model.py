from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

# Data cleaning
# .read_csv converts the document to an array
df=pd.read_csv('./dataset/penguins_lter.csv')

print(df)
df = df.drop(['Comments', 'Region', 'Sample Number', 'studyName', 'Stage', 'Individual ID', 'Delta 15 N (o/oo)', 'Clutch Completion', 'Date Egg', 'Delta 13 C (o/oo)'], axis=1)

df['Species'] = df['Species'].replace({
    'Adelie Penguin (Pygoscelis adeliae)': 1,
    'Gentoo penguin (Pygoscelis papua)': 2,
    'Chinstrap penguin (Pygoscelis antarctica)': 3
})
# male-0 female-1

df['Sex'] = df['Sex'].replace({'MALE':0,'FEMALE':1})
df['Island'] = df['Island'].replace({'Torgersen':0,'Biscoe':1,'Dream':2})

df=df.dropna()

df=df[df['Sex']!='.']



# Cleaned Data for model

train,test=train_test_split(df,test_size=0.23)

# Data for training model
train_x=train[['Island','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)','Sex']]
train_y=train[['Species']] 

# Data for testing model
test_x=test[['Island','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)','Sex']]
test_y=test[['Species']]

# Data fitting in model

rfc=RandomForestClassifier()
rfc.fit(train_x,train_y)


pickle.dump(rfc,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))