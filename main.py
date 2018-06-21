# The goal is to create a list of word-patterns based on certain letter combinations in the English language.
# Source: https://github.com/Sheyin/word-unscrambler

from functions import unscramble, postfixIsInLetterPool, filterKnownLetters, printResults, filterResultsLackingVowels, filterUnusualResults, invalidInput
import word
from copy import copy
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
	return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
	raw_letters = request.args.get('letters', '')
	num_spaces_input = request.args.get('length', '')
	known_input = request.args.get('known', '')
	knownLetters = request.args.get('knownLetters', '')

	invalid, invalidReason, known = invalidInput(raw_letters, num_spaces_input, known_input, knownLetters)
	if invalid:
		print(invalidReason)
		return render_template('error.html', reason=invalidReason)

	# Only do these after input has been checked
	num_spaces = int(num_spaces_input)
	solutions = []

	letters = list(raw_letters.lower())

	# Check if these letters are a subset of the list of letters, then display combinations
	for combination in word.postfixes:
		if postfixIsInLetterPool(copy(letters), combination):
			solutions += unscramble(copy(letters), combination, num_spaces, solutions)

	if known:
		solutions = filterKnownLetters(solutions, knownLetters)

	filteredSolutions = []
	solutions, filteredSolutions = filterUnusualResults(solutions)
	if num_spaces > 4:
		solutions, filteredSolutions = filterResultsLackingVowels(solutions)
	# sort() didn't seem to work, but sorted() does - requires a new variable though
	sortedSolutions = sorted(solutions, key=str.lower)
	sortedFilteredSolutions = sorted(filteredSolutions, key=str.lower)

	return render_template('results.html', numResults=len(solutions), letters=raw_letters, solutions=sortedSolutions, filteredSolutions=sortedFilteredSolutions, numFiltered=len(filteredSolutions))
