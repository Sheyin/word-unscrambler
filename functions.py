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
# Spaces: length of the word to find
# Solutions: List of results to be appended to, with results from this function running w/ other postfixes
# How this works is that it looks at the pool of letters as a set ('letters').  If the 'postfix'
# (here, 'subset) is in this pool, it removes the letters from the pool, then determines combinations
# ('permutations', combinations is probably the more appropriate term though) of the remaining letters,
# affixing the postfix onto each combination.
# So for example, letters 'stamp' - subset 'amp' - removes 'amp' leaving 'st' as the remaining letters.
# It would determine two combinations - st and ts - and append 'amp' to each, returning a list with
# 'stamp' and 'tsamp' as the results.
def unscramble(letters, subset, spaces, solutions):
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


# This checks to see if the letters of the postfix ('subset') are in the pool of letters ('letters')
# It returns false upon detecting a letter is not present in the pool, so the calling method
# doesn't attempt to unscramble using this postfix.  Otherwise, it will return true allowing it to run.
def postfixIsInLetterPool(letters, subset):
    for _ in subset:
        try:
            letters.remove(_)
        except ValueError:
            return False
    else:
        return True


# This uses a regular expression to check whether a letter in a given position matches
# a 'known letter' position given by the user.  If it matches, the result is copied to
# another list that will be returned to the calling method.
# Ex. in a crossword, you may know that the word will have 5 blanks, and starts with 'st',
# so 'st' would be the known letters.  This method would check 'st...' against every result,
# copying the ones that match to filteredSolutions, and ignoring the rest.
def filterKnownLetters(solutions, knownLetters):
	filteredSolutions = []
	# Reformats the list of known letters to be a regular expression
	def buildRegularExpression():
		expression = ""
		for character in knownLetters:
			if character in ['', ' ', '.', ';', ',', '_']:
				expression += '.'
			else:
				expression += character
			# Note to self - assignments go into innermost scope, causing nested error - https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping
		return expression

	expression = buildRegularExpression()
	regex = re.compile(expression)

	for word in solutions:
		if re.match(regex, word):
			filteredSolutions.append(word)
	return filteredSolutions


# Tries to filter out some of the junk results by eliminating words without a vowel in the first few spaces
# It should only be called if the word is a certain length (>4), since there are 3-letter words with no vowels.
def filterResultsLackingVowels(solutions):
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


# Prints results, hopefully in columns, for easier reading.  Only for console version.
def printResults(solutions):
    columnCounter = 1
    for text in solutions:
        if columnCounter % 4 == 0:
            print("   " + text)
        else:
            print("   " + text, end='')
        columnCounter += 1



# Not yet complete.  Trying to implement checking for specialConsonantPairs with a regular expression
#def checkStartingConsonants(substring):
	#vowelString = ''.join(word.vowels)
	#vowelExpression = '[' + vowelString + ']'
	#consonantExpression = '[^' + vowelString + ']'
	#expression = vowelExpression + '(?=)' + consonantExpression
	#regex = re.compile(expression)
	#if re.match(regex, substring):
