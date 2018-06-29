# The goal is to create a list of word-patterns based on certain letter combinations in the English language.
# Source: https://github.com/Sheyin/word-unscrambler

from functions import invalidInput, formatInput, generateCombinations
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
		return render_template('error.html', reason=invalidReason)

	# Only do these after input has been checked
	letters, numSpaces, known, knownLetters = formatInput(lettersInput, knownInput, numSpacesInput, knownLettersInput)
	postfixResults, nonPostfixResults, oddLetterResults, lackingVowelResults = generateCombinations(letters, numSpaces, known, knownLetters)
	totalCount = len(postfixResults) + len(nonPostfixResults) + len(oddLetterResults) + len(lackingVowelResults)

	return render_template('results.html', letters=''.join(letters), totalCount= totalCount, postfixResults=postfixResults, postfixCount=len(postfixResults),
		nonPostfixResults=nonPostfixResults, nonPostfixCount=len(nonPostfixResults), oddLetterResults=oddLetterResults, oddLetterCount=len(oddLetterResults),
		lackingVowelResults=lackingVowelResults, lackingVowelCount=len(lackingVowelResults))
