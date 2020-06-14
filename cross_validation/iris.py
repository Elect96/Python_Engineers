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

iris_data = load_iris()
print(iris_data)