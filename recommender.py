import pandas as pd
import numpy as np
import sklearn as skl 
import csv

class Recommender:

    # These DataFrames will contain all the information about the movies that will be used
    # to train the recommender.
    tags = pd.read_csv('./links.csv')
    movies = pd.read_csv('./IMDbmovies.csv', low_memory=False)
    ratings = pd.read_csv('./ratings.csv')
    movieInfo = pd.read_csv('movies_metadata.csv')

    # Dataset cleaning
    movies = movies.fillna(0)
    movies['imdb_title_id'] = movies['imdb_title_id'].astype(str)
    movies['imdb_title_id'] = movies['imdb_title_id'].str.replace('tt', '')

    tags['imdbId'] = '0' + tags['imdbId'].astype(str)

    # Crosstab that accumulates user ratings and movie ID's
    ratings = ratings.head(50000)
    ratings.to_csv('ratingsSmall.csv')
    ct = pd.pivot_table(ratings, values = 'rating', columns = ['movieId'], index = ['userId'] )

    # MovieID will contain a list of recommendations that will accumulate over a single use
    # of the program

    # userTaste will be a Series that contains the user's ratings of the calibration moviess
    
    # getRecommendation() will add movie recommendations to the MovieID pd.Series every time it is call,
    # it will make sure that the movie has not already been recommended.
    def getRecommendation(self):
        return 0
        

    def __init__(self, uT):
        self.userTaste = uT


r = Recommender(pd.Series([0,0,0,0]))
print(r.userTaste)
print(r.movies.head())
print(r.tags.head())
print(r.ratings.head(20))
print(r.ratings.userId.drop_duplicates())
print(r.ct.loc[1,858])
print(r.ct)