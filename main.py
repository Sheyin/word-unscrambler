# The goal is to create a list of word-patterns based on certain letter combinations in the English languageself.

from functions import unscramble
import word
from copy import copy

print("Enter the letters given:")
raw_letters = input()

# TODO: Sanitize input

letters = list(raw_letters)
print("Letters: " + str(letters) + " Number of letters entered: " + str(len(letters)))

# Check if these letters are a subset of the list of letters, then display combinations
for combination in word.postfixes:
    #if set(list(combination)).issubset(letters):
    # This works but gives false positives in duplicate letters in the subset (ex. -ene is triggered on "nrge")
    if set(list(combination)).issubset(letters):
        print(combination + " is a subset of " + raw_letters + ".")
        print("Debug: letters is: " + str(letters))
        unscramble(copy(letters), combination, "postfix")
