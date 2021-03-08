#import stuff
import sys
import pandas

class Options:
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

	output = ""
	_genre = ""
	_director = ""
	_minReleaseYr = -1
	_maxReleaseYr = -1
	userTaste = array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	#Recommender, no pointer exists in python?
	
	#void
	def getUserOptions():
		ratings=input("What movie rating guideline do you want (G, PG, PG-13, R,NC-17)press none if not applicable")
		language= input("What language should the movie be in (French, German, English, Hindi, etc),press none if not applicable")
		genre= input("What genre of movies do you want to watch(Historical Fiction, Documentry, Science Fiction, etc)press none if not applicable")
		director= input("What director's movie do you want to watch (ex Christopher Nolan, George Lucas, Steven Spielberg, James Cameron)press none if not applicable")
	def getUserTaste():
		print('Rate the following movies out of a 1-5 scale \(1 being worst, 5 being best\)')
		print('To skip a movie, type \"-1\"\n')
	
	#get user ratings of movies
	#placeholder until proper movei database is implemented

		var1 = input('placeholder\n')
		while(((var1 < 1) or (var1 > 5)) and (var1 != -1)):
		var1 = input('Wrong input, please choose a number between 1-5\n')
		var2 = input('placeholder\n')
		while(((var2 < 1) or (var2 > 5)) and (var2 != -1)):
                var2 = input('Wrong input, please choose a number between 1-5\n')

		var3 = input('placeholder\n')
		while(((var3 < 1) or (var3 > 5)) and (var3 != -1)):
                var3 = input('Wrong input, please choose a number between 1-5\n')

		var4 = input('placeholder\n')
		while(((var4 < 1) or (var4 > 5)) and (var4 != -1)):
                var4 = input('Wrong input, please choose a number between 1-5\n')
	
		var5 = input('placeholder\n')
        	while(((var5 < 1) or (var5 > 5)) and (var5 != -1)):
                var5 = input('Wrong input, please choose a number between 1-5\n')

		var6 = input('placeholder\n')
        	while(((var6 < 1) or (var6 > 5)) and (var6 != -1)):
                var6 = input('Wrong input, please choose a number between 1-5\n')

		var7 = input('placeholder\n')
        	while(((var7 < 1) or (var7 > 5)) and (var7 != -1)):
                var7 = input('Wrong input, please choose a number between 1-5\n')

		var8 = input('placeholder\n')
        	while(((var8 < 1) or (var8 > 5)) and (var8 != -1)):
                var8 = input('Wrong input, please choose a number between 1-5\n')

		var9 = input('placeholder\n')
        	while(((var9 < 1) or (var9 > 5)) and (var9 != -1)):
                var9 = input('Wrong input, please choose a number between 1-5\n')

		var10 = input('placeholder\n')
        	while(((var10 < 1) or (var10 > 5)) and (var10 != -1)):
                var10 = input('Wrong input, please choose a number between 1-5\n')

	#assign all values to vector

		userTaste = array([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10])
	def giveUserRecs():
	#bool
	def approveMovie(movieID):
