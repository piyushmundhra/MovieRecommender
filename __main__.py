import pandas as pd
import numpy as np
from optpkg.rpkg.recommender import Recommender
from optpkg.userOptions import userOptions
from optpkg.options1 import Options1
from optpkg.Options2 import Options2

def is_not_integer(i):
		try: 
			int(i)
			return False
		except ValueError:
			return True

# uo is a userOptions object
def program(uo):

    uo.getUserOptions()
    uo.getUserTaste()
    uo.giveUserRecs()
    temp1 = ""

    while(temp1 != '0'):
        print('\n\nWhat would you like to do now? \n0 - Restart program \n1 - Get more recommendations \n2 - Exit program')

        valid1 = False
        while(valid1 == False):
            temp1 = input()
            if(is_not_integer(temp1)):
                print('\nInvalid input. Please enter either \'0\', \'1\', or \'2\'.\n')
            else:
                if( ((int(temp1) != 0) & (int(temp1) != 1)) & (int(temp1) != 2) ):
                    print('\nInvalid input. Please enter either \'0\', \'1\', or \'2\'.\n')
                    continue
                else:
                    valid1 = True

        if(int(temp1) == 0):
            main()
        elif(int(temp1) == 1):
            uo.giveUserRecs()
        else:
            return


# main harness that utilizes program()
def main():
    print("If you have no idea what you want to watch, please enter \'0\'")
    print("If you want to see movies similar to a movie you like, please enter \'1\'\n")

    userChoice = -1

    valid1 = False
    temp1 = ""
    while(valid1 == False):
        temp1 = input()
        if(is_not_integer(temp1)):
            print('\nInvalid input. Please enter either \'0\' or \'1\'.\n')
        else:
            if( (int(temp1) != 0) & (int(temp1) != 1) ):
                print('\nInvalid input. Please enter either \'0\' or \'1\'.\n')
                continue
            else:
                valid1 = True
    userChoice = int(temp1)
    if(userChoice == 1):
        u = Options2()
        program(u)
    else:
        u = Options1()
        program(u)


main()