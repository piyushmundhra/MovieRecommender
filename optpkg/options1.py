import sys
import pandas as pd
from optpkg.userOptions import userOptions
from optpkg.rpkg.recommender import Recommender

class Options1(userOptions):
	currentPosition = 0
	movieVec = pd.Series(["0114709", "0076759", "5013056", "1320244"])
	userTaste = pd.Series([0,0,0,0])
	r = Recommender()
	
	def getUserOptions(self):
		#no options
		return 0

	def getUserTaste(self):
		
		print("Please rate the following movies. If you like the movie, type 1. If you don't like, don't care about or haven't watched the movie, type -1.")
		
		print("\n\nToy Story")
		temp1=int(input())
		
		while((temp1 != -1) & (temp1 != 1)):
    			temp1 = int(input('\nInvalid input. please enter either 1 or -1\n'))
		self.userTaste.loc[0] = temp1
	
		print("\n\nThe Godfather")
		temp2=int(input())

		while((temp2 != -1) & (temp2 != 1)):
			temp2 = int(input('\nInvalid input. please enter either 1 or -1\n'))
		self.userTaste.loc[1] = temp2


		print("\n\nStar Wars: Episode IV-A New Hope")
		temp3=int(input())

		while((temp3 != -1) & (temp3 != 1)):
				temp3 = int(input('\nInvalid input. please enter either 1 or -1\n'))
		self.userTaste.loc[2] = temp3

		print("\n\nNightmare on Elm Street")
		temp4=int(input())

		while((temp4 != -1) & (temp4 != 1)):
				temp4 = int(input('\nInvalid input. please enter either 1 or -1\n'))
		self.userTaste.loc[3] = temp3
		
	def giveUserRecs(self):
		if(self.currentPosition > 3):
			print("Sorry, out of recommendations. Please restart the program!")
		print("Here is a list of recommended movies for you:\n")
		if(self.userTaste.loc[self.currentPosition] == 1):
  			print(self.r.getRecommendation(
    				self.r.imdbToMovie(self.movieVec[self.currentPosition]))
  			)	
  			self.currentPosition = self.currentPosition + 1
		else:
  			self.currentPosition = self.currentPosition + 1
  			self.giveUserRecs()
		


