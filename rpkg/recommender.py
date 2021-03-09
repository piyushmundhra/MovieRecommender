# recommender system based on: https://towardsdatascience.com/a-simple-movie-recommendation-system-d135cfd0a22d

import pandas as pd
import numpy as np
import csv
import warnings
warnings.filterwarnings('ignore')


class Recommender:
    # These DataFrames will contain all the information about the movies that will be used
    # to train the recommender.

    # GitHub has limited file size so datasets will be stored remotely on Google Drive

    # tags : pd.DataFrame
    tags = pd.read_csv('data/links.csv', low_memory=False)
    tags = tags.astype(str)
    tags['imdbId'] = '0'+tags['imdbId']

    # movies : pd.DataFrame
    movies = pd.read_csv('data/movies.csv', low_memory=False)

    # ratings : pd.DataFrame
    ratings = pd.read_csv('data/ratings.csv', low_memory=False)

    # movieInfo : pd.DataFrame
    movieInfo = pd.read_csv('data/tags.csv', low_memory=False)

    # Crosstab that accumulates user ratings and movie ID's
    ct1 = pd.pivot_table(ratings, values = 'rating', columns = ['movieId'], index = ['userId'] )

    # id : string : imdbId of movie
    def imdbToMovie(self, id):
        temp = self.tags[self.tags['imdbId'] == id]
        temp = temp.reset_index()
        return int(temp.iloc[0,1])


    # getRecommendation() will add movie recommendations to the MovieID pd.Series every time it is call,
    # it will make sure that the movie has not already been recommended.
    def getRecommendation(self, mvId):

        # isolates ratings of the current movie being used for recommendation
        shrekRatings = self.ct1.loc[:,mvId]

        # computes the pairwise correlation of the selected movie and all other movies 
        rec = self.ct1.corrwith(shrekRatings)
        rec = rec.dropna()
        recdf = pd.DataFrame(rec, columns=['correlation'])

        # creates a DataFrame containing information about the number of ratings per movie
        filtered = self.ratings.groupby('movieId').size()
        filteredDF = pd.DataFrame(filtered, columns=['size'])

        # movie names 
        nms = self.movies.set_index('movieId')['title']
        nmsdf = pd.DataFrame(nms, columns=['title'])

        # creates a dataframe that contains all the movieId's, and the corresponding correlation and sample size
        semifinal = recdf.join(filteredDF)
        semifinal = semifinal.join(nmsdf)

        # filters the semifinal dataframe based on sample size (number of ratings must be at least 100)
        final = semifinal[semifinal['size'] > 100]
        final = final.sort_values(['correlation'], ascending=False)
        final = final.reset_index()
        return final['title'][0:10]
        

    def __init__(self, uT):
        self.userTaste = uT





