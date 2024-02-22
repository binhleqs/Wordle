#This is simple project for wordle game

#Import libs
import random_word
from PyDictionary import PyDictionary

#Set-up the game 

randomWords = random_word.RandomWords()
dict = PyDictionary()

word = randomWords.get_random_word()
meaning = dict.meaning(word)
print(word)
print(meaning.get("Noun")[0])