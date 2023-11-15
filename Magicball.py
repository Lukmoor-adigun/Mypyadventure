# Function that generates random number and gives output base on number
# generated from another function.

import random
# This function returns output.
def Nineball(yourAnswer):
    if (yourAnswer == 1):
        return 'It is one'
    elif (yourAnswer == 2):
        return 'Your input is two'
    elif (yourAnswer == 3):
        return 'Your input is three'
    elif (yourAnswer == 4):
        return 'Your input is four'
    elif (yourAnswer == 5):
        return 'Your input is Five'
    elif (yourAnswer == 6):
        return 'Your input is Six'
    elif (yourAnswer == 7):
        return 'Your input is Seven'
    elif (yourAnswer == 8):
        return 'Your input is Eight'
    elif (yourAnswer == 9):
        return 'Your input is Nine'
    else:
        return 'None'
# This function generates random number.  
def numGen(a,b):
    generator = random.randint(a,b)
    return generator

genNum = numGen(1,9)
finalResult = Nineball(genNum)
print(finalResult)