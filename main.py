# The goal is to create a list of word-patterns based on certain letter combinations in the English languageself.

from functions import unscramble, checkDuplicateLetters, filterKnownLetters, printResults
import word
from copy import copy

print("Enter the letters given:")
raw_letters = input()

print("How many letters is the word?: ")
num_spaces = int(input())

print("Are there any known spaces?: ")
confirmKnownSpaces = input()
knownLetters = []

if ('y' in confirmKnownSpaces.lower()):
    for counter in range(0, num_spaces):
        print("What is in slot " + str(counter + 1) + "? Press space or enter if not known.")
        knownLetters.append(input().lower())

solutions = []

# TODO: Check inputs for validity before proceeding

letters = list(raw_letters.lower())

# Check if these letters are a subset of the list of letters, then display combinations
for combination in word.postfixes:
    if set(list(combination)).issubset(letters):
        if checkDuplicateLetters(copy(letters), combination):
            solutions += unscramble(copy(letters), combination, "postfix", num_spaces, solutions)

if ('y' in confirmKnownSpaces.lower()):
    solutions = filterKnownLetters(solutions, knownLetters)

print("Current # of solutions: " + str(len(solutions)))

# TODO: Recheck filtering duplicate entries - appears to be showing up again
# - Also, removing invalid letter placement isn't working reliably - case "sldoit" / 4 space / (i, 1), (o, 3)
# - Perhaps removed items are being readded to the list, invalidating entire loop

printResults(solutions)

print("\n--- End ---")
