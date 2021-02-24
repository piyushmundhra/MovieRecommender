import pandas as pd
import numpy as np
import sklearn as skl 
import csv

class Recommender:
    # These DataFrames will contain all the information about the movies that will be used
    # to train the recommender.

    # GitHub has limited file size so datasets will be stored remotely on Google Drive

    # tags : pd.DataFrame
    urltags = 'https://drive.google.com/file/d/1_AHvEpjmG9u3HHXcme1W21vD91tQjXAc/view?usp=sharing'
    pathtags = 'https://drive.google.com/uc?export=download&id=' + urltags.split('/')[-2]
    tags = pd.read_csv(pathtags)

    # movies : pd.DataFrame
    movies = pd.read_csv('./IMDbmovies.csv', low_memory=False)

    # ratings : pd.DataFrame
    ratings = pd.read_csv('./ratingsSmall.csv')
    ratingsbig = pd.read_csv('./ratings.csv')

    # movieInfo : pd.DataFrame
    movieInfo = pd.read_csv('movies_metadata.csv')

    # Crosstab that accumulates user ratings and movie ID's
    ct1 = pd.pivot_table(ratings, values = 'rating', columns = ['movieId'], index = ['userId'] )

    # MovieID will contain a list of recommendations that will accumulate over a single use
    # of the program

    # userTaste will be a Series that contains the user's ratings of the calibration moviess
    
    # getRecommendation() will add movie recommendations to the MovieID pd.Series every time it is call,
    # it will make sure that the movie has not already been recommended.
    def getRecommendation(self):
        return 0
        

    def __init__(self, uT):
        self.userTaste = uT
        # Dataset cleaning
        self.movies = self.movies.fillna(0)
        self.movies['imdb_title_id'] = self.movies['imdb_title_id'].astype(str)
        self.movies['imdb_title_id'] = self.movies['imdb_title_id'].str.replace('tt', '')

        self.tags['imdbId'] = '0' + self.tags['imdbId'].astype(str)


r = Recommender(pd.Series([0,0,0,0]))
print(r.movies.head())
print(r.tags.head())
print(r.ratings.head())
print(r.ratingsbig.head())
print(r.ct1)

