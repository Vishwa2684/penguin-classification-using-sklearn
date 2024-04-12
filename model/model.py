# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Ignore FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)


# %% [markdown]
# <h1>EXTRAPOLATORY DATA ANALYSIS & DATA CLEANING</h1>

# %%
# .read_csv converts the document to an array
df=pd.read_csv('../dataset/penguins_lter.csv')

#removing unnecessary columns in dataframe which are not used in penguin classification

df = df.drop(['Comments', 'Region', 'Sample Number', 'studyName', 'Stage', 'Individual ID', 'Delta 15 N (o/oo)', 'Clutch Completion', 'Date Egg', 'Delta 13 C (o/oo)'], axis=1)

df['Species'] = df['Species'].replace({
    'Adelie Penguin (Pygoscelis adeliae)': 1,
    'Gentoo penguin (Pygoscelis papua)': 2,
    'Chinstrap penguin (Pygoscelis antarctica)': 3
})
# male-0 female-1

df['Sex'] = df['Sex'].replace({'MALE':0,'FEMALE':1})
df['Island'] = df['Island'].replace({'Torgersen':0,'Biscoe':1,'Dream':2})

print("DataFrame size:",np.shape(df)[0],"X",np.shape(df)[1])
df

# %% [markdown]
# <h1>get information about data</h1>

# %%


# we can get a specific column using pandas

# There is no problem in our dataset (no empty columns)
# Now our task is to split data
df.info()

# %%
#get description of data
df.describe(include='all')
df['Island'].unique()

# %%
df.info()

# %% [markdown]
# <h1>After getting information about the dataframe we check NaN values in DataFrame using</h1>
# - DataFrame.isna().sum()

# %%
df.isna().sum()

# %%
#removing rows containing NaN 
df=df.dropna()
df

# %%
df['Sex'].unique()

# %%
#get unique values in every column of dataframe
for i in df:
    print(df[i].unique())
# Filter the dataframe where value of sex is not .
df=df[df['Sex']!='.']
# df    

# %%


# %% [markdown]
# <h1>FILTERING OF DATA IS DONE</h1> 
# - NOW WE VIEW GRAPHICAL REPRESENTATION OF DATA

# %%
ax=sns.countplot(x='Species',data=df)
ax.bar_label(ax.containers[0])

# %%
ax=sns.countplot(x='Island',data=df)
ax.bar_label(ax.containers[0])

# %%
# Get a heat map with annotations
print(  df.corr(numeric_only=True))
sns.heatmap(df[['Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)']].corr(),annot=True,cmap='RdBu')
# CONSIDER A FEATURE IN HEATMAP WHICH IS HIGHLY CORRELATED

# %% [markdown]
# <h1>We're done with the analysis of data</h1>
# - Now we split data for training and testing for it we use sklearn
# 
# <u><strong>Note:</strong></u>
# <h3>If your output (y) is a string and u don't encode the string, you'll face the following error</h3>
# <img src="../screenshots/ValueError.jpg"/>

# %%


# %%
from sklearn.model_selection import train_test_split
train,test=train_test_split(df,test_size=0.23)

train_x=train[['Island','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)','Sex']]
train_y=train[['Species']]

test_x=test[['Island','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)','Sex']]
test_y=test[['Species']]
test_x
test_y


# %% [markdown]
# <h1>PICKING UP A MODEL WHICH CAN CLASSIFY THE PENGUIN</h1>
#     <ul>
#         <li>So the given problem is a classification problem</li>
#         <li>Im going to use Random Forest Classifier because in this problem we classify which type of penguin it is.</li>
#     </ul>

# %%
from sklearn.ensemble import RandomForestClassifier

#Using RandomForestClassifier because in the given problem we are classifying between 3 objects
rfc=RandomForestClassifier()
rfc.fit(train_x,train_y)

# %% [markdown]
# <h1>Now the model is prepared after fitting the training data in it</h1>
#  - Time to test the model by making predictions

# %%
from sklearn.metrics import accuracy_score,confusion_matrix

# Giving test inputs to model for predictions
predicted_labels=rfc.predict(test_x)

# to check accuracy we compare our test output with test input

print(accuracy_score(test_y,predicted_labels))

# 

confusion_mat=confusion_matrix(test_y,predicted_labels)

plt.figure(figsize=(8,6))
sns.heatmap(confusion_mat,annot=True,fmt='d',cmap='Blues')
plt.title('confusion matrix')
plt.xlabel('prediction label')
plt.ylabel('truth')
plt.show()

# Note:{
#     'Adelie Penguin (Pygoscelis adeliae)': 1,
#     'Gentoo penguin (Pygoscelis papua)': 2,
#     'Chinstrap penguin (Pygoscelis antarctica)': 3
# }


