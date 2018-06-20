# The goal is to create a list of word-patterns based on certain letter combinations in the English language.

from functions import unscramble, postfixIsInLetterPool, filterKnownLetters, printResults, filterResultsLackingVowels
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
	known_input = request.args.get('known', '')
	# This is necessary because Python bool() only checks the string is empty or not
	known = False
	if known_input == "True":
		known = True
	knownLetters = request.args.get('knownLetters', '')
	solutions = []

	# TODO: Check inputs for validity before proceeding

	letters = list(raw_letters.lower())

	# Check if these letters are a subset of the list of letters, then display combinations
	for combination in word.postfixes:
		# Testing removing this since the inner loop is doing the same thing
		#if set(list(combination)).issubset(letters):
		if postfixIsInLetterPool(copy(letters), combination):
			solutions += unscramble(copy(letters), combination, num_spaces, solutions)

	if known:
		solutions = filterKnownLetters(solutions, knownLetters)

	# Making this >4 because of irregularities, such as "pry", which would cause all
	# results to be filtered, since it would see 'pr', no vowel, and then remove it.
	# The "filtered solutions" will still be displayed but underneath the normal results.
	filteredSolutions = []
	if num_spaces > 4:
		solutions, filteredSolutions = filterResultsLackingVowels(solutions)
	numFiltered = len(filteredSolutions)

	# TODO: Recheck filtering duplicate entries - appears to be showing up again

	return render_template('results.html', numResults=len(solutions), letters=raw_letters, solutions=solutions, filteredSolutions=filteredSolutions, numFiltered=numFiltered)
