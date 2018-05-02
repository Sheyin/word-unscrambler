# The goal is to create a list of word-patterns based on certain letter combinations in the English language.

from functions import unscramble, checkDuplicateLetters, filterKnownLetters, printResults, removeResults
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

preFilteredSolutionsCount = len(solutions)

# Making this >3 because of irregularities, such as "pry"
if num_spaces > 4:
	solutions, filteredSolutions = removeResults(solutions)

# TODO: Recheck filtering duplicate entries - appears to be showing up again

print("\nSolutions: (" + (str(len(solutions))) + " found)")
printResults(solutions)
print("\nUnlikely Solutions: (" + (str(len(filteredSolutions))) + " found)")
printResults(filteredSolutions)
print("\nCurrent # of solutions: " + str(len(solutions)) + " Unlikely: " + str(preFilteredSolutionsCount - len(solutions)))

print("\n--- End ---")
