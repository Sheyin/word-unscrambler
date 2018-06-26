# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools
import re
import textwrap
from math import ceil
from word import softConsonants, startWithExceptions, illegalStartingVowelPairings, vowels, consonants, vowelExceptions, postfixes, hardConsonants, softConsonantPairsLegal


# Begins entire combination process (Formerly in main)
# Multiple lists are being returned so they can all be displayed on a page with reason for filtering.
def generateCombinations(letters, numSpaces, known, knownLetters):
	allResults = []
	allCombinations = itertools.permutations(letters, numSpaces)
	for _ in allCombinations:
		combination = ''.join(_)
		# Filtering some duplicates caused by multiple copies of a letter
		if combination not in allResults:
			allResults.append(combination)

	if known:
		allResults = filterKnownLetters(allResults, knownLetters)

	# Filters out results starting with odd letter combinations
	filteredResults, oddLetterResults = filterUnusualResults(allResults)

	lackingVowelsResults = []
	# Filters out results lacking vowels in the first half of the word
	if numSpaces > 4:
		filteredResults, lackingVowelsResults = filterResultsLackingVowels(filteredResults)

	# Filters out results not ending in the list of postfixes defined in word.py
	postfixResults, nonPostfixResults = filterNonPostfixCombinations(filteredResults)

	return sorted(postfixResults, key=str.lower), sorted(nonPostfixResults, key=str.lower), sorted(oddLetterResults, key=str.lower), sorted(lackingVowelsResults, key=str.lower)



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
			if character == '_':
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


# Tries to filter words based on the beginning characters - most words will never start with certain
# combinations of letters, though there are exceptions.
def filterUnusualResults(solutions):
	# This is to simplify the second else branch since there are so many conditions.
	# Returns True if illegal, False if it is okay
	def isIllegalStartingConsonant():
		if word[0] == word[1]:
			# Making an exception only for llamas
			if len(word) == 5 and word == 'llama' or len(word) == 6 and word == 'llamas':
				return False

		# This is basically saying, if both 1-2 are in softConsonants
		if word[0] in softConsonants and word[1] in softConsonants:
			# No words starting with these letters followed by another consonant
			if word[0] in ['h', 'l', 'n', 'y']:
				return True
			elif word[0:2] in softConsonantPairsLegal:
				return False

		# There's probably some amount of exceptions to this....
		elif word[0] in hardConsonants and word[1] in softConsonants:
			return False

		# These are for very specific hard consonant pairings
		elif word[0:2] in startWithExceptions:
			return False
		return True

	trimmedSolutions = []
	unlikelySolutions = []

	for word in solutions:
		# If starts with vowel, allow all but words starting with certain vowel-vowel pairings.
		if word[0] in vowels:
			if word[0:2] in illegalStartingVowelPairings:
				unlikelySolutions.append(word)
			else:
				trimmedSolutions.append(word)
		# Starts with consonant, if second character is a vowel or 'soft consonant', allow.
		# Else, reject unless first two letters is in startsWithExceptions.
		else:
			if word[1] in vowels or not isIllegalStartingConsonant():
				trimmedSolutions.append(word)
			else:
				unlikelySolutions.append(word)
	return trimmedSolutions, unlikelySolutions


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


# Combinations that don't fit the "known postfixes" in words.py will be put into a separate list
def filterNonPostfixCombinations(solutions):
	matchedResults = []
	unmatchedResults = []
	matched = False
	# For each postfix, if the postfix matches the ending of the word, then move to results list
	for combination in solutions:
		for ending in postfixes:
			regex1 = re.compile(ending + '$')
			regex2 = re.compile(ending + 's$')
			if not matched and re.search(regex1, combination):
				# The last few letters matched something in postfixes
				matched = True
			elif not matched and 's' in combination and re.search(regex2, combination):
				matched = True
		if matched:
			matchedResults.append(combination)
		else:
			unmatchedResults.append(combination)
		matched = False
	return matchedResults, unmatchedResults


# Used for validating input.  Returns true if something is invalid and what caused the error.
# Note that re.match only checks the beginning of the string, while re.search checks it all.
def invalidInput(lettersInput, numSpacesInput, knownInput, knownLettersInput):
	# Checking letter input for non-letter input
	if lettersInput == "":
		return True, "Error: No letters given to search."
	elif len(lettersInput) < 3:
		return True, "Error: This tool was only designed for words of at least length 3."
	else:
		regex = re.compile('[^a-zA-Z]+')
		if re.search(regex, lettersInput):
			return True, "Error: Invalid input detected in letters.  Must be letters a-z only."

	# Checking numSpacesInput for numeric input only
	if numSpacesInput == "":
		return True, "Error: Length of word to search for was not given."
	else:
		regex = re.compile('[^0-9]+')
		if re.search(regex, numSpacesInput):
			return True, "Error: Invalid input detected in number of letters.  Must be numeric digits, 0-9 only."
		elif int(numSpacesInput) == 0:
			return True, "Error: The word you are searching for has a length of 0."
		elif int(numSpacesInput) in range(1,3):
			return True, "Error: This tool was only designed for words of at least length 3."

	# Checking known_letters for valid input.  If unknown, it should be replaced with a _ in the info sent to the server.
	# It is legal to be empty (though shouldn't do anything) and knownInput should be false.
	if knownInput == "True":
		if knownLettersInput == "":
			return True, "Error: It was indicated that there were known letters, but no letters/positions were given."
		else:
			regex = re.compile('[^a-zA-Z_]+|[\d]+')
			if re.search(regex, knownLettersInput):
				return True, "Error: the known letters can only contain the letters a-z."
			else:
				# At this point, known letters consists of legal input a-z or _ if it is an unknown letter
				regex = re.compile('[a-zA-Z]+')
				result = re.search(regex, knownLettersInput)
				if not re.search(regex, knownLettersInput):
					return True, "Error: It was indicated that there were known letters, but no letters/positions were given."
				# Check if each of the known letters is in the letters given
				for _ in knownLettersInput:
					if _ is not '_' and _.lower() not in lettersInput.lower():
						return True, "Error: Known letter '" + _ + "' is not in the pool of letters given."
				# There should technically be a case here for "if letters were given but knownInput is false" but making it so the letters are disregarded.
	elif knownInput not in ['True', 'False', '']:
		return True, "...Are you messing with something you shouldn't be?  Either you know letters in the word, or you don't."

	# At this point, everything is good
	return False, ""


# Formats the input from the strings received in the request to the proper formats
def formatInput(lettersInput, knownInput, numSpacesInput, knownLettersInput):
	letters = list(lettersInput.lower())
	# This is necessary because Python bool() only checks the string is empty or not
	if knownInput == "True":
		known = True
	else:
		known = False

	return letters, int(numSpacesInput), known, knownLettersInput.lower()
