#! /usr/bin/python
# src: https://www.pythonforengineers.com/machine-learning-for-complete-beginners/
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import  joblib
pd.options.mode.chained_assignment = None

# data read
data = pd.read_csv("titanic_test.csv")

# model input
data_input = data[['pclass', 'sex']]

# data clean-up
print(data_input.head())
data_input['sex'] = np.where(data_input['sex'] == "female", 0, 1)
data_input['pclass'].replace("3rd", 3, inplace=True)
data_input['pclass'].replace("2nd", 2, inplace=True)
data_input['pclass'].replace("1st", 1, inplace=True)
print(data_input.head())

expected_output = data[['survived']]

# training
input_train, input_test, expected_output_train, expected_output_test = \
    train_test_split(data_input, expected_output, test_size=.33, random_state=42)

# start the learning
rf = RandomForestClassifier(n_estimators=100)
rf.fit(input_train, expected_output_train)
accuracy = rf.score(input_test, expected_output_test)
print("Accuracy: {}%".format(accuracy * 100))

# save the model to a file
joblib.dump(rf, "titanic_model_2", compress=9)