from abc import ABC, abstractmethod 
from optpkg.rpkg.recommender import Recommender

class userOptions(ABC):
    r = Recommender()
    
    @abstractmethod
    def getUserOptions(self):
        pass

    @abstractmethod
    def getUserTaste(self):
        pass

    @abstractmethod
    def giveUserRecs(self):
        pass

    @abstractmethod
    def approveMovies(self):
        pass