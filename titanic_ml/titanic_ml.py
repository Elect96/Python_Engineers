#! /usr/bin/python
# src: https://www.pythonforengineers.com/machine-learning-for-complete-beginners/
import numpy as np
import pandas as pd
# machine learning algorithm
from sklearn.ensemble import RandomForestClassifier
# test train split
from sklearn.model_selection import train_test_split
# switch off pandas warning
pd.options.mode.chained_assignment = None
# write the model to a file
from sklearn.externals import joblib

# data read
data = pd.read_csv("titanic_train.csv")

# model inputs
data_inputs = data[['pclass', 'age', 'sex']]

# data clean-up
median_age = data['age'].median()
data_inputs['age'].fillna(median_age, inplace=True)
data_inputs['age'] = data_inputs['age'].astype("int")
data_inputs['pclass'].replace("3rd", 3, inplace=True)
data_inputs['pclass'].replace("2nd", 2, inplace=True)
data_inputs['pclass'].replace("1st", 1, inplace=True)
data_inputs['sex'] = np.where(data_inputs['sex'] == "female", 0, 1)

expected_output = data[['survived']]
# test_size .33 means 33% of the sample is to be used to testing, the rest go for training
# random_state is used to initialise the inbuilt randomiser, so we get the same result from the randomiser each time
input_train, input_test, expected_output_train, expected_output_test = \
    train_test_split(data_inputs, expected_output, test_size=.33, random_state=42)

# start machine learning
rf = RandomForestClassifier(n_estimators=100)
# fit() is used to train the algorithm
rf.fit(input_train, expected_output_train)
# check the accuracy

