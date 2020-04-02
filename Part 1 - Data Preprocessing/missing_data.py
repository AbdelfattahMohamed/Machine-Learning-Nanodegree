# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
# i want to solve this problem by get the mean for nan values
# i can get mean || median || mod

# sklearn library import Imputer from missing data "Don't forget that for missing data"
from sklearn.preprocessing import Imputer

# axis =0 col & axis= 1 row
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# fit -> calculate it on the range in fit[......]
imputer = imputer.fit(X[:, 1:3])    # the values in rows in 2 columns 
X[:, 1:3] = imputer.transform(X[:, 1:3]) #put the result in X[]


#Encoding Categorical Data
#_____________FOR TEST THIS CASE: X in the console___________
#using Sklearn
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# why x -> because of the independent var " in this case country"
labelencoder_X = LabelEncoder() 
# i will take place this on all rows in first column "Country"
X[ : , 0 ]= labelencoder_X.fit_transform(X[ : ,0])
#we have a problem right now ""Dummy var""
#------------solve it by Onehot Encoding-------------
onehotencoder = OneHotEncoder(categorical_features = [0])   #index 0 for first col
X = onehotencoder.fit_transform(X).toarray()
#perdect work for test  run X
# we need to make the dependent variabe but not one hot encoding because of we need 1 or 0 only
labelencoder_y = LabelEncoder() 
y= labelencoder_y.fit_transform(y)


#================================= splitting data ==========================
#we use this library for split 



