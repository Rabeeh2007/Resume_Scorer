import numpy as np
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
pd.set_option('display.max_columns', None)
df = pd.read_csv("final.csv")
df.replace({'Domain':{"Cybersecurity":5,"Software Engineering":4,"Machine Learning":3,"Data Science":2,"Blockchain":1}},inplace=True)

def model():
    x = df.drop(columns=["Final_score"])
    y = df["Final_score"]
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.25,random_state=4)
    model = LinearRegression()
    model.fit(xtrain,ytrain)
    joblib.dump(model,"model.pkl")
    a = model.predict(xtest)
    error = mean_squared_error(a,ytest)
    print(error)

model()