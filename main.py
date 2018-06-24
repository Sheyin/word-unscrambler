# The goal is to create a list of word-patterns based on certain letter combinations in the English language.
# Source: https://github.com/Sheyin/word-unscrambler

from functions import unscramble, postfixIsInLetterPool, filterKnownLetters, printResults, filterResultsLackingVowels, filterUnusualResults, invalidInput, formatInput, generateCombinations
import word
from copy import copy
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
	return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
	lettersInput = request.args.get('letters', '')
	numSpacesInput = request.args.get('length', '')
	knownInput = request.args.get('known', '')
	knownLettersInput = request.args.get('knownLetters', '')

	invalid, invalidReason = invalidInput(lettersInput, numSpacesInput, knownInput, knownLettersInput)
	if invalid:
		print(invalidReason)
		return render_template('error.html', reason=invalidReason)

	# Only do these after input has been checked
	letters, numSpaces, known = formatInput(lettersInput, knownInput, numSpacesInput)
	generateCombinations(lettersInput, numSpaces, known, knownLettersInput)

	solutions = []

	# Check if these letters are a subset of the list of letters, then display combinations
	for combination in word.postfixes:
		if postfixIsInLetterPool(copy(letters), combination):
			solutions += unscramble(copy(letters), combination, numSpaces, solutions)

	if known:
		solutions = filterKnownLetters(solutions, knownLettersInput)

	filteredSolutions = []
	solutions, filteredSolutions = filterUnusualResults(solutions)
	if numSpaces > 4:
		solutions, filteredSolutions = filterResultsLackingVowels(solutions)
	# sort() didn't seem to work, but sorted() does - requires a new variable though
	sortedSolutions = sorted(solutions, key=str.lower)
	sortedFilteredSolutions = sorted(filteredSolutions, key=str.lower)

	return render_template('results.html', numResults=len(solutions), letters=lettersInput, solutions=sortedSolutions, filteredSolutions=sortedFilteredSolutions, numFiltered=len(filteredSolutions))
