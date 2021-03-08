#import stuff


class userOptions:
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
	def getUserTaste():
	def giveUserRecs():
	#bool
	def approveMovie(movieID):
