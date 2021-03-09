from abc import ABC, abstractmethod 
from ..rpkg import recommender
from recommender import Recommender

class userOptions(ABC):
    output = ""
    r = Recommender()

    def getUserOptions(self):
        pass
    def getUserTaste(self):
        pass
    def giveUserRecs(self):
        pass
    def approveMovies(self):
        pass