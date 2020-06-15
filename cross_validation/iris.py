#! /usr/bin/python
# src: https://www.pythonforengineers.com/cross-validation-and-model-selection/
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# iris data load
iris_data = load_iris()

# input / output data
data_input = iris_data.data
data_output = iris_data.target

# K fold
# 5 folds/splits; shuffle means randomise the data
kf = KFold(5, shuffle=True)

# random forest
rf_class = RandomForestClassifier(n_estimators=10)
# logistic regression
log_class = LogisticRegression()
# SVM
svm_class = svm.SVC()

print("Random Forests: ")
print(cross_val_score(rf_class, data_input, data_output, scoring="accuracy", cv=10))
accuracy = cross_val_score(rf_class, data_input, data_output, scoring="accuracy", cv=10).mean() * 100
print("Accuracy of Random Forests is: ", accuracy)

print("\nLogistic Regression: ")
print(cross_val_score(log_class, data_input, data_output, scoring="accuracy", cv=10))
accuracy = cross_val_score(log_class, data_input, data_output, scoring="accuracy", cv=10).mean() * 100
print("Accuracy of Logistic Regression is: ", accuracy)

print("\nSVM: ")
print(cross_val_score(svm_class, data_input, data_output, scoring="accuracy", cv=10))
accuracy = cross_val_score(svm_class, data_input, data_output, scoring="accuracy", cv=10).mean() * 100
print("Accuracy of SVM is: ", accuracy)

# fix the warnings by specifying arguments at log_class and svm_class
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

