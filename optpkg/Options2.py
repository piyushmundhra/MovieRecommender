
#import stuff
import sys
import pandas
from optpkg.userOptions import userOptions
from optpkg.rpkg.recommender import Recommender
class Options2(userOptions):
	
	numMovies=0
	movieID=""
	r= Recommender()
	def getUserOptions(self):
		temp=int(input("How many movies do you want in yout recommendation list? Please put a whole number up to 15.")
 		
		if( ((0<temp) & (temp<16)) ):
			numMovies=temp
		else:
			print("Invalid input, Please try again")
			self.getUserOptions()
	def getUserTaste(self):
		temp2=input("Please enter the IMDB movie ID from the IMDB website. it will be in the form tt0372784")
		temp2 = temp2.replace('tt', '')
		if(r.has_movie(temp2)):
			movieID=temp2
		else:
			print("Invalid input, Please try again")
			self.getUserTaste()
	def giveUserRecs(self):
		print("Here's the list of the recommended movies for you")
		print(r.getRecommendation(r.imdbToMovie(movieID)[0:numMovies]))
	
		
