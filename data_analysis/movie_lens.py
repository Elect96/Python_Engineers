#! /usr/bin/python
# src: https://www.pythonforengineers.com/data-analysis-with-pandas/
import pandas as pd
import matplotlib.pyplot as plt

user_columns = ['user_id', 'age', 'gender']
users = pd.read_csv("u.user", sep="|", names=user_columns, usecols=range(3))

rating_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv("u.data", sep="\t", names=rating_columns, usecols=range(3))

movie_columns = ['movie_id', 'title']
movies = pd.read_csv("u.item", sep="|", names=movie_columns, usecols=range(2), encoding="iso-8859-1")

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
movie_data = pd.merge(movie_ratings, users, on="user_id")
# top rated movies
# print("Top rated movies (overall): \n", movie_data.groupby("title").size().sort_values(ascending=False)[:20])

# people > 60
oldies = movie_data[(movie_data.age > 60)]
oldies = oldies.groupby("title").size().sort_values(ascending=False)

# teens
teens = movie_data[(movie_data.age > 12) & (movie_data.age < 20)]
teens = teens.groupby("title").size().sort_values(ascending=False)

# print("Top 10 movies for oldies: \n", oldies[:10])
# print("Top 10 movies for teens: \n", teens[:10])

# popular 250
ratings_by_title = movie_data.groupby("title").size()
popular_movies = ratings_by_title.index[ratings_by_title >= 250]

# ratings by gender
ratings_by_gender = movie_data.pivot_table("rating", index="title", columns="gender")
# print("Rated movies by gender: \n", ratings_by_gender)

# ratings by gender for popular_movies
ratings_by_gender = ratings_by_gender.loc[popular_movies]
# print(ratings_by_gender)

# top rated by women
top_movies_women = ratings_by_gender.sort_values(by="F", ascending=False)
# print("Top rated movies by women: \n", top_movies_women.head())

# add a new column
ratings_by_gender['diff'] = ratings_by_gender['M'] - ratings_by_gender['F']
# print("Difference by gender: \n", ratings_by_gender.head())

# greatest difference in votes
gender_diff = ratings_by_gender['diff']
gender_diff = abs(gender_diff)
gender_diff.sort_values(inplace=True, ascending=False)

# show top 10 differences
gender_diff[:10].plot(kind="barh")
plt.show()