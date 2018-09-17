"""
GIS 5578, Python lists game
@author: dahaynes
"""

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

hangmanWords = ["garbage"]
correctLetter = []

for word in hangmanWords:
    print("%s" % ("_ "* len(word)))

    for tries in range(0,10):
        userLetter = input("Please enter in a letter: ")

        #Check to see if the letter is in the alphabet
        
                
            #Check to see if the letter is in the word
                correctLetter.append(userLetter)
                if l in correctLetter:
                    print(l)
                else:
                    print("_")
            #Remove letters from the alphabet
        else:
            print("try again")