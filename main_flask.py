# The goal is to create a list of word-patterns based on certain letter combinations in the English language.

from functions import unscramble, checkDuplicateLetters, filterKnownLetters, printResults, removeResults
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
	num_spaces = int(request.args.get('length', ''))
	known = bool(request.args.get('known', ''))
	knownLetters = request.args.get('knownLetters', '')
	solutions = []

	# TODO: Check inputs for validity before proceeding

	letters = list(raw_letters.lower())

	# Check if these letters are a subset of the list of letters, then display combinations
	for combination in word.postfixes:
		if set(list(combination)).issubset(letters):
			if checkDuplicateLetters(copy(letters), combination):
				solutions += unscramble(copy(letters), combination, "postfix", num_spaces, solutions)

	if known:
	    solutions = filterKnownLetters(solutions, knownLetters)

	# Making this >3 because of irregularities, such as "pry"
	filteredSolutions = []
	if num_spaces > 3:
		solutions, filteredSolutions = removeResults(solutions)
	numFiltered = len(filteredSolutions)

	# TODO: Recheck filtering duplicate entries - appears to be showing up again

	return render_template('results.html', numResults=len(solutions), letters=raw_letters, solutions=solutions, filteredSolutions=filteredSolutions, numFiltered=numFiltered)
