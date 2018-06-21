# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools
import re
import textwrap
from math import ceil
from word import softConsonants, startWithExceptions, illegalStartingVowelPairings, vowels, consonants, vowelExceptions

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
			# TODO: May want to make this less permissive - only _ for blanks
			if character in ['', ' ', '.', ';', ',', '_']:
				expression += '.'
			else:
				expression += character.lower()
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
	# Checks if a subset (vowel, letter pair, etc) is present in a (sub)string; (firstHalfOfWord) returns a boolean value
	def checkForSubset():
		vowelsAndExceptions = vowels + vowelExceptions
		for _ in vowelsAndExceptions:
			if _ in firstHalfOfWord:
				return True
		return False

	trimmedSolutions = []
	unlikelySolutions = []

	for word in solutions:
		halfWordLength = int(ceil(len(word) / 2))
		firstHalfOfWord = word[0:halfWordLength]

		# Checks if there is a vowel or exception to vowel in the first half of the word
		if(checkForSubset()):
			trimmedSolutions.append(word)
		else:
			unlikelySolutions.append(word)

	return trimmedSolutions, unlikelySolutions


# Tries to filter words based on the beginning characters - most words will never start with certain
# combinations of letters, though there are exceptions.
def filterUnusualResults(solutions):
	trimmedSolutions = []
	unlikelySolutions = []

	for word in solutions:
		# If starts with vowel, allow all but words starting with certain vowel-vowel pairings.
		if word[0] in vowels:
			if word[1] in vowels and word[0:2] in illegalStartingVowelPairings:
				unlikelySolutions.append(word)
			else:
				trimmedSolutions.append(word)
		# Starts with consonant, if second character is a vowel or 'soft consonant', allow.
		# Else, reject unless first two letters is in startsWithExceptions.
		else:
			if word[1] in vowels or word[1] in softConsonants or word[0:2] in startWithExceptions:
				trimmedSolutions.append(word)
			else:
				unlikelySolutions.append(word)
	return trimmedSolutions, unlikelySolutions



# Used for validating input.  Returns true if something is invalid and what caused the error.
# Note that re.match only checks the beginning of the string, while re.search checks it all.
def invalidInput(raw_letters, num_spaces, known_input, knownLetters):
	# Checking letter input for non-letter input
	if raw_letters == "":
		return True, "Error: No letters given to search.", False
	elif len(raw_letters) < 3:
		return True, "Error: This tool was only designed for words of at least length 3.", False
	else:
		regex = re.compile('[^a-zA-Z]+')
		if re.search(regex, raw_letters):
			return True, "Error: Invalid input detected in letters.  Must be letters a-z only.", False

	# Checking num_spaces for numeric input only
	if num_spaces == "":
		return True, "Error: Length of word to search for was not given.", False
	else:
		regex = re.compile('[^0-9]+')
		if re.search(regex, num_spaces):
			return True, "Error: Invalid input detected in number of letters.  Must be numeric digits, 0-9 only.", False
		elif int(num_spaces) == 0:
			return True, "Error: The word you are searching for has a length of 0.", False
		elif int(num_spaces) in range(1,3):
			return True, "Error: This tool was only designed for words of at least length 3.", False

	# Checking known_letters for valid input.  If unknown, it should be replaced with a _ in the info sent to the server.
	# It is legal to be empty (though shouldn't do anything) and known_input should be false.
	if known_input == "True":
		if knownLetters == "":
			return True, "Error: It was indicated that there were known letters, but no letters/positions were given.", False
		else:
			regex = re.compile('[^a-zA-Z_]+|[\d]+')
			if re.search(regex, knownLetters):
				return True, "Error: the known letters can only contain the letters a-z.", False
			else:
				# At this point, known letters consists of legal input a-z or _ if it is an unknown letter
				regex = re.compile('[a-zA-Z]+')
				result = re.search(regex, knownLetters)
				if not re.search(regex, knownLetters):
					return True, "Error: It was indicated that there were known letters, but no letters/positions were given.", False
				# Check if each of the known letters is in the letters given
				for _ in knownLetters:
					if _ is not '_' and _ not in raw_letters:
						return True, "Error: Known letter '" + _ + "' is not in the pool of letters given.", False
				# There should technically be a case here for "if letters were given but known_input is false" but making it so the letters are disregarded.
	elif known_input not in ['True', 'False', '']:
		return True, "...Are you messing with something you shouldn't be?  Either you know letters in the word, or you don't.", False

	# At this point, everything is good
	# This is necessary because Python bool() only checks the string is empty or not
	if known_input == "True":
		return False, "", True
	else:
		return False, "", False


# Prints results, hopefully in columns, for easier reading.  Only for console version.
def printResults(solutions):
    columnCounter = 1
    for text in solutions:
        if columnCounter % 4 == 0:
            print("   " + text)
        else:
            print("   " + text, end='')
        columnCounter += 1
