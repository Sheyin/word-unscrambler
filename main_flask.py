# The goal is to create a list of word-patterns based on certain letter combinations in the English language.

from functions import unscramble, checkDuplicateLetters, filterKnownLetters, printResults
import word
from copy import copy
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def start():
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

    print("Current # of solutions: " + str(len(solutions)))

    # TODO: Recheck filtering duplicate entries - appears to be showing up again

    printResults(solutions)

    print("\n--- End ---")

    return render_template('results.html', numResults=len(solutions), letters=raw_letters, solutions=solutions)
