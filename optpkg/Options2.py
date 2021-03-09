
#import stuff
import sys
import pandas
from optpkg.userOptions import userOptions
from optpkg.rpkg.recommender import Recommender

class Options2(userOptions):

	numMovies = 0
	movieID = ""
	r = Recommender()
	
	def is_not_integer(self, i):
		try: 
			int(i)
			return False
		except ValueError:
			return True

	def getUserOptions(self):
		print("How many movies do you want in your recommendation list? Please enter a whole number in between 1 and 10 (inclusive).\n")
 		
		valid1 = False
		temp1 = ""
		while(valid1 == False):
			temp1 = input()
			if(self.is_not_integer(temp1)):
				print('\nInvalid input. Please enter a whole number in between 1 and 10 (inclusive).\n')
			else:
				if( (int(temp1) > 10) | (int(temp1) < 1) ):
					print('\nInvalid input. Please enter a whole number in between 1 and 10 (inclusive).\n')
					continue
				else:
					valid1 = True
		self.numMovies = int(temp1)


	def getUserTaste(self):
		temp2=input("Please enter the IMDB movie ID from the IMDB website. \nYou can find it in the url of the desired movie's page, it will be in the form \'tt1234567\'\n")
		temp2 = temp2.replace('tt', '')
		
		if(self.r.has_movie(temp2)):
			self.movieID=temp2
		else:
			print("Invalid input, Please try again")
			self.getUserTaste()

	def giveUserRecs(self):
		print("Here's the list of the recommended movies for you\n")
		print(
			self.r.getRecommendation(
				self.r.imdbToMovie(self.movieID),
				self.numMovies
			) 
		)	
		
		
	
		
