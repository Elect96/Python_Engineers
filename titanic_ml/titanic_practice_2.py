#! /usr/bin/python
# src: https://www.pythonforengineers.com/machine-learning-for-complete-beginners/
import numpy as np
import pandas as pd
# machine learning algorithm
from sklearn.ensemble import RandomForestClassifier
# test train split
from sklearn.model_selection import train_test_split
# write the model to a file
from sklearn.externals import joblib
# switch off pandas warning
pd.options.mode.chained_assignment = None

# data read
data = pd.read_csv("titanic_train.csv")

# data clean-up
data_input = data[['pclass', 'sex']]
data_input.replace("3rd", 3, inplace=True)
data_input.replace("2nd", 2, inplace=True)
data_input.replace("1st", 1, inplace=True)
data_input['sex'] = np.where(data_input['sex'] == "female", 0, 1)

# outcome
expected_outcome = data[['survived']]
input_train, input_test, expected_output_train, expected_output_test = \
    train_test_split(data_input, expected_output, test_size=.33, random_state=42)
# load the model
rf = joblib.load("titanic_model_2")

# make a prediction
pred = rf.predict(data_input)

# calculate accuracy
accuracy = rf.score(data_input, pred)
print("Accuracy: {}%".format(accuracy * 100))

# sort out the outcome, it shows 100% accuracy which is for sure wrong