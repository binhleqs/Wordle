#This is simple project for wordle game

#Import libs
import random_word
from PyDictionary import PyDictionary

#Set-up the game 

randomWords = random_word.RandomWords()
dict = PyDictionary()

#generate a simple words
result = None
while result is None: 
    try:
        word = randomWords.get_random_word()
        meanings = dict.meaning(word)
        
        if len(word) <= 6 and meanings != None :
            meaning = meanings.get("Noun")
            result = True
    except:
        print("There was a problem")


print(word)
num_letter = len(word)
# get the first meaning in dictionary

print("The word has {} letters".format(num_letter))
print("□"*num_letter)
print(meaning)

 
