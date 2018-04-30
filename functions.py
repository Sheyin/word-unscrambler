# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools
import re
import textwrap
from math import ceil
from word import vowels, vowelExceptions, specialConsonantPairs

# Letters: the pool of letters to choose from
# Subset: a detected combination of letters to exclude from the pool and build combinations upon
def unscramble(letters, subset, type, spaces, solutions):
    numLettersToRemove = len(letters) - spaces
    solution = []
    # Remove the first instance of each letter of subset from the pool
    for character in subset:
        letters.remove(character)

    # If there is only 1 s, and it is being used in the subset, then skip the plural
    # AND make sure it obeys the # of spaces requested
    if ('s' not in subset and letters.count('s') >= 1) or ('s' in subset and letters.count('s') >= 2):
        pluralLetters = copy(letters)
        pluralLetters.remove('s')
        pluralResults = itertools.permutations(pluralLetters)

        for pluralPermutation in pluralResults:
            pluralCombination = ''.join(pluralPermutation) + subset
            pluralCombination = pluralCombination[numLettersToRemove:]
            pluralCombination += 's'

            if pluralCombination not in solution and pluralCombination not in solutions:
                solution.append(pluralCombination)


    results = itertools.permutations(letters)

    for permutation in results:
        combination = ''.join(permutation) + subset
        combination = combination[numLettersToRemove:]
        if combination not in solution:
            solution.append(combination)
    return solution


def checkDuplicateLetters(letters, subset):
    for _ in subset:
        try:
            letters.remove(_)
        except ValueError:
            return False
    else:
        return True


# Keeps only the words that match a letter in the position of a known letter
# TODO: Maybe remove words that don't include any vowels, etc (or y)
def filterKnownLetters(solutions, knownLetters):
    filteredSolutions = []

    expression = buildRegularExpression(knownLetters)
    regex = re.compile(expression)

    for word in solutions:
        if re.match(regex, word):
            filteredSolutions.append(word)
    return filteredSolutions


# Tries to filter out some of the junk results by eliminating words without a vowel in the first few spaces
def removeResults(solutions):
	trimmedSolutions = []
	unlikelySolutions = []

	for word in solutions:
		halfWordLength = int(ceil(len(word) / 2))
		firstHalfOfWord = word[0:halfWordLength]

		# Checks if there is a vowel or exception to vowel in the first half of the word
		if(checkForSubset(firstHalfOfWord)):
			trimmedSolutions.append(word)
		else:
			unlikelySolutions.append(word)
	return trimmedSolutions, unlikelySolutions


# Checks if a subset (vowel, letter pair, etc) is present in a (sub)string; returns a boolean value
def checkForSubset(substring):
	vowelsAndExceptions = vowels + vowelExceptions
	for _ in vowelsAndExceptions:
		if _ in substring:
			return True
	return False


# Not yet complete.  Trying to implement checking for specialConsonantPairs with a regular expression
#def checkStartingConsonants(substring):
	#vowelString = ''.join(word.vowels)
	#vowelExpression = '[' + vowelString + ']'
	#consonantExpression = '[^' + vowelString + ']'
	#expression = vowelExpression + '(?=)' + consonantExpression
	#regex = re.compile(expression)
	#if re.match(regex, substring):



# Reformats the list of known letters to be a regular expression
def buildRegularExpression(knownLetters):
    expression = ""
    for character in knownLetters:
        if character in ['', ' ', '.', ';', ',', '_']:
            expression += '.'
        else:
            expression += character
    return expression


# Prints results, hopefully in columns, for easier reading.
def printResults(solutions):
    columnCounter = 1
    for text in solutions:
        if columnCounter % 4 == 0:
            print("   " + text)
        else:
            print("   " + text, end='')
        columnCounter += 1
