#! /usr/bin/python
# src: https://www.pythonforengineers.com/machine-learning-for-complete-beginners/
import numpy as np
import pandas as pd
# write the model to a file
from sklearn.externals import joblib
# switch off pandas warning
pd.options.mode.chained_assignment = None


def find_error(prediction):
    titanic_data = np.loadtxt("titanic_results.txt", dtype="int32")
    diff = np.equal(titanic_data, prediction)
    correct_answers = np.sum(diff)
    percent_diff = correct_answers / len(prediction) * 100
    print("Titanic: Percentage Match is: ", percent_diff)


# data read
data = pd.read_csv("titanic_test.csv")

# data clean-up
data_input = data[['pclass', 'sex']]
data_input.replace("3rd", 3, inplace=True)
data_input.replace("2nd", 2, inplace=True)
data_input.replace("1st", 1, inplace=True)
data_input['sex'] = np.where(data_input['sex'] == "female", 0, 1)

# load the model
rf = joblib.load("titanic_model_2")

# make a prediction
pred = rf.predict(data_input)

# model accuracy
find_error(pred)
