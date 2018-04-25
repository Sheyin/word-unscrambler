# The goal is to create a list of word-patterns based on certain letter combinations in the English languageself.

from functions import unscramble, checkDuplicateLetters
import word
from copy import copy

print("Enter the letters given:")
raw_letters = input()

print("How many letters is the blank?: ")
num_spaces = int(input())
#num_spaces = 5

# TODO: Sanitize inputs

letters = list(raw_letters.lower())
#print("Letters: " + str(letters) + " Number of letters entered: " + str(len(letters)))

# Check if these letters are a subset of the list of letters, then display combinations
for combination in word.postfixes:
    #if set(list(combination)).issubset(letters):
    # This works but gives false positives in duplicate letters in the subset (ex. -ene is triggered on "nrge")
    #setLetters = set(letters)
    #setCombination = set(list(combination))
    #setIntersection = setLetters.intersection(setCombination)
    #if setIntersection == setCombination and len(setIntersection) == len(setCombination):
    #    print("Debug: intersection: " + str(setLetters.intersection(setCombination)))
    if set(list(combination)).issubset(letters):
        # Need a second test to check for duplicate elements, which are not filtered by set functions
        if checkDuplicateLetters(copy(letters), combination):
            print(combination + " is a subset of " + raw_letters + ".")
            unscramble(copy(letters), combination, "postfix", num_spaces)

print("--- End ---")
