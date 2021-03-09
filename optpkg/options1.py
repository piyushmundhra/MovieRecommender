import sys
import pandas
from optpkg.userOptions import userOptions
from optpkg.rpkg.recommender import Recommender

class Options1(userOptions):
	currentPosition = 0;
	movieVec = pd.Series(["0114709", "0076759", "5013056", "1320244"])
	userTaste = pd.Series([0,0,0,0])
	r = Recommender()
	
	def getUserOptions(self):
		#no options
	def getUserTaste(self):
		
		print("Please rate the following movies. If you like the movie, type 1. If you don't like, don't care about or haven't watched the movie, type -1.")
		
		print("\n\nToy Story")
		temp1=input()
		
		while(temp1 != -1 & temp1 != 1):
    			temp1 = input('\nInvalid input. please enter either 1 or -1')
		self.userTaste.loc[0] = temp1
	
		print("\n\nThe Godfather")
                temp2=input()

                while(temp2 != -1 & temp2 != 1):
                        temp2 = input('\nInvalid input. please enter either 1 or -1')
		self.userTaste.loc[1] = temp2


		print("\n\nStar Wars: Episode IV-A New Hope")
                temp3=input()

                while(temp3 != -1 & temp3 != 1):
                        temp3 = input('\nInvalid input. please enter either 1 or -1')
		self.userTaste.loc[2] = temp3

		print("\n\nNightmare on Elm Street")
                temp4=input()

                while(temp4 != -1 & temp4 != 1):
                        temp4 = input('\nInvalid input. please enter either 1 or -1')
		self.userTaste.loc[3] = temp3
		
	def giveUserRecs(self):
		print("Here is a list of recommended movies for you:\n")
		if(self.userTaste.loc[self.currentPosition] == 1):
  			print(self.r.getRecommendation(
    				self.r.imdbToMovie(self.movieVec[self.currentPosition]))
  			)	
  			self.currentPosition = self.currentPosition + 1
		else:
  			self.currentPosition = self.currentPosition + 1
  			self.giveUserRecs()
		


