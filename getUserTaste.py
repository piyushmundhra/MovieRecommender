#function, not a class
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

#def checkCorrectInput(passInVal):
#	if ((passInVal < 1) or (passInVal > 5)):
 #		return false
	
	
