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
    urlmovies = 'https://drive.google.com/file/d/1lacw_PaUsvlzpRemtnAfcKqGSkx1JBbY/view?usp=sharing'
    pathmovies = 'https://drive.google.com/uc?export=download&id=' + urlmovies.split('/')[-2]
    movies = pd.read_csv(pathmovies, low_memory=False)

    # ratings : pd.DataFrame
    urlratings = 'https://drive.google.com/file/d/1m4nj5Mf36sWq_8bfT_e0TiibyGo22s2p/view?usp=sharing'
    pathratings = 'https://drive.google.com/uc?export=download&id=' + urlratings.split('/')[-2]
    ratings = pd.read_csv(pathratings)

    # movieInfo : pd.DataFrame
    urlMI = 'https://drive.google.com/file/d/1b_Jmt75aZRBh2z5TxYXnOsA17l81H_TJ/view?usp=sharing'
    pathMI = 'https://drive.google.com/uc?export=download&id=' + urlMI.split('/')[-2]
    movieInfo = pd.read_csv(pathMI)

    # Dataset cleaning
    movies = movies.fillna(0)
    movies['imdb_title_id'] = movies['imdb_title_id'].astype(str)
    movies['imdb_title_id'] = movies['imdb_title_id'].str.replace('tt', '')

    tags['imdbId'] = '0' + tags['imdbId'].astype(str)

    # Crosstab that accumulates user ratings and movie ID's
    ct1 = pd.pivot_table(ratings, values = 'rating', columns = ['movieId'], index = ['userId'] )

    
    # getRecommendation() will add movie recommendations to the MovieID pd.Series every time it is call,
    # it will make sure that the movie has not already been recommended.
    def getRecommendation(self):
        return 0
        

    def __init__(self, uT):
        self.userTaste = uT


r = Recommender(pd.Series([0,0,0,0]))
print(r.movies.shape)
print(r.tags.shape)
print(r.ratings.head())
print(r.ct1)

