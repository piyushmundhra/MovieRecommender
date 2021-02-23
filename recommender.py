import pandas as pd
import numpy as np

class Recommender:

    # These DataFrames will contain all the information about the movies that will be used
    # to train the recommender.
    tags = pd.read_csv('')
    movies = pd.read_csv('')
    ratings = pd.read_csv('')
    movieInfo = pd.read_csv('')

    # MovieID will contain a list of recommendations that will accumulate over a single use
    # of the program
    movieID = pd.Series()

    # userTaste will be an Series that contains the user's ratings of the calibration moviess
    userTaste = pd.Series()
    
    def getRecommendation(self):
        return 0
        
    def __init__(self, uT):
        self.userTaste = uT


