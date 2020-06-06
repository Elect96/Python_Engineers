#! /usr/bin/python
# src: https://www.pythonforengineers.com/data-analysis-with-pandas/
import pandas as pd
import matplotlib.pyplot as plt

user_columns = ['user_id', 'age', 'sex']
users = pd.read_csv("u.user", sep="|", names=user_columns, usecols=range(3))

rating_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv("u.data", sep="\t", names=user_columns, usecols=range(3))

movie_columns = ['movie_id', 'title']
movies = pd.read_csv("u.item", sep="|", names=movie_columns, usecols=range(2), encoding="iso-8859-1")
# print(movies.keys())

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
movie_data = pd.merge(movie_ratings, users, on="user_id")
# print(movie_ratings)
# top rated movies
print("Top rated movies (overall): \n", movie_data.groupby("title").size().sort_values(ascending=False)[:20])

