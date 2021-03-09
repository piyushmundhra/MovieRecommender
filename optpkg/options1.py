import sys
import pandas as pd
from optpkg.userOptions import userOptions
from optpkg.rpkg.recommender import Recommender

class Options1(userOptions):
	currentPosition = 0
	movieVec = pd.Series(["0114709", "0372784", "0076759", "1179056"])
	userTaste = pd.Series([-1,-1,-1,-1])
	r = Recommender()
	
	def getUserOptions(self):
		#no options
		return 0
	def is_not_integer(self, i):
		try: 
			int(i)
			return False
		except ValueError:
			return True

	def getUserTaste(self):
		
		print("Please rate the following movies. If you like the movie, type 1. If you don't like, don't care about or haven't watched the movie, type 0.")
		
		print("\n\nToy Story (1995)")
		valid1 = False
		temp1 = ""
		while(valid1 == False):
			temp1 = input()
			if(self.is_not_integer(temp1)):
				print('\nInvalid input. please enter either 1 or 0\n')
			else:
				if( (int(temp1) != 1) & (int(temp1) != 0) ):
					print('\nInvalid input. please enter either 1 or 0\n')
					continue
				else:
					valid1 = True
		self.userTaste.loc[0] = int(temp1)
		
	
		print("\n\nBatman Begins (2005)")
		valid2 = False
		temp2 = ""
		while(valid2 == False):
			temp2 = input()
			if(self.is_not_integer(temp2)):
				print('\nInvalid input. please enter either 1 or 0\n')
			else:
				if( (int(temp2) != 1) & (int(temp2) != 0) ):
					print('\nInvalid input. please enter either 1 or 0\n')
					continue
				else:
					valid2 = True
		self.userTaste.loc[1] = int(temp2)


		print("\n\nStar Wars: Episode IV-A New Hope")
		valid3 = False
		temp3 = ""
		while(valid3 == False):
			temp3 = input()
			if(self.is_not_integer(temp3)):
				print('\nInvalid input. please enter either 1 or 0\n')
			else:
				if( (int(temp3) != 1) & (int(temp3) != 0) ):
					print('\nInvalid input. please enter either 1 or 0\n')
					continue
				else:
					valid3 = True
		self.userTaste.loc[2] = int(temp3)

		print("\n\nNightmare on Elm Street")
		valid4 = False
		temp4 = ""
		while(valid4 == False):
			temp4 = input()
			if(self.is_not_integer(temp4)):
				print('\nInvalid input. please enter either 1 or 0\n')
			else:
				if( (int(temp4) != 1) & (int(temp4) != 0) ):
					print('\nInvalid input. please enter either 1 or 0\n')
					continue
				else:
					valid4 = True
		self.userTaste.loc[3] = int(temp4)
		
	def giveUserRecs(self):
		print(self.currentPosition)
		if(self.currentPosition > 3):
			print("Sorry, out of recommendations. Please restart the program!")
		else:	
			if(self.userTaste.loc[self.currentPosition] == 1):
				print("Here is a list of recommended movies for you:\n")
				print(
					self.r.getRecommendation(
						self.r.imdbToMovie(self.movieVec.loc[self.currentPosition])
					) 
				)	
				self.currentPosition = self.currentPosition + 1
				return
			else:
				self.currentPosition = self.currentPosition + 1
				self.giveUserRecs()
		


