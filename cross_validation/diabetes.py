#! /usr/bin/python
# src: https://www.pythonforengineers.com/cross-validation-and-model-selection/
# dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.model_selection import train_test_split

# data load
headers = ['num_times_pregnant', 'glucose_level', 'blood_pres', 'skin_thickness', 'insulin', 'bmi', 'dia_pedigree', 'age', 'has_diabetes']
data = pd.read_csv("pima-indians-diabetes.data", names = headers)

# i/o data
input_data = data[['num_times_pregnant', 'glucose_level', 'blood_pres', 'skin_thickness', 'insulin', 'bmi', 'dia_pedigree', 'age']]
expected_output = data['has_diabetes']

# random forest
rf = RandomForestClassifier(n_estimators=10)
# logistic regression
lr = LogisticRegression(solver="lbfgs", multi_class="auto", max_iter=1000)
# svm
svm = svm.SVC(gamma="scale")

# cross__val_score mean for 3 algorithms
print("Random Forest: ")
print(cross_val_score(rf, input_data, expected_output, scoring="accuracy", cv=10))
accuracy = cross_val_score(rf, input_data, expected_output, scoring="accuracy", cv=10).mean() * 100
print("Accuracy of Random Forest is: ", accuracy)

print("\nLinear Regression: ")
print(cross_val_score(lr, input_data, expected_output, scoring="accuracy", cv=10))
accuracy = cross_val_score(lr, input_data, expected_output, scoring="accuracy", cv=10).mean() * 100
print("Accuracy of Linear Regression is: ", accuracy)

print("\nSVM: ")
print(cross_val_score(svm, input_data, expected_output, scoring="accuracy", cv=10))
accuracy = cross_val_score(svm, input_data, expected_output, scoring="accuracy", cv=10).mean() * 100
print("Accuracy of SVM is: ", accuracy)

# test/train split
x_train, x_test, y_train, y_test = train_test_split(input_data, expected_output, test_size=.33)

# rf training
print("\nAlgorithms scores: ")
rf.fit(x_train, y_train)
print("RF: ", rf.score(x_test, y_test))
# lr training
lr.fit(x_train, y_train)
print("LR: ", lr.score(x_test, y_test))
# svm training
svm.fit(x_train, y_train)
print("SVM: ", svm.score(x_test, y_test))
