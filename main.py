# The goal is to create a list of word-patterns based on certain letter combinations in the English language.
# Source: https://github.com/Sheyin/word-unscrambler

from functions import invalidInput, formatInput, generateCombinations
import word
import secret
from copy import copy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = secret.uri
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def start():
    return render_template('index.html', title="Search for a word")


@app.route('/search', methods=['GET'])
def search():
    lettersInput = request.args.get('letters', '')
    numSpacesInput = request.args.get('length', '')
    knownInput = request.args.get('known', '')
    knownLettersInput = request.args.get('knownLetters', '')

    print("Received: ")
    print("Letters: " + lettersInput + " numSpaces: " + numSpacesInput +
          " knownInput: " + knownInput + " knownLettersInput: " + knownLettersInput)

    invalid, invalidReason = invalidInput(
        lettersInput, numSpacesInput, knownInput, knownLettersInput)
    if invalid:
        return render_template('error.html', title="Error!", reason=invalidReason)

    # Only do these after input has been checked
    letters, numSpaces, known, knownLetters = formatInput(
        lettersInput, knownInput, numSpacesInput, knownLettersInput)
    print("After formatting:")
    print("Letters: " + str(letters) + " numSpaces: " + str(numSpaces) +
          " known: " + str(known) + " knownLetters: " + str(knownLetters))
    postfixResults, nonPostfixResults, oddLetterResults, lackingVowelResults = generateCombinations(
        letters, numSpaces, known, knownLetters)
    totalCount = len(postfixResults) + len(nonPostfixResults) + \
        len(oddLetterResults) + len(lackingVowelResults)

    return render_template('results.html', title="Results for '" + ''.join(letters) + "'", letters=''.join(letters), totalCount=totalCount, postfixResults=postfixResults, postfixCount=len(postfixResults),
                           nonPostfixResults=nonPostfixResults, nonPostfixCount=len(nonPostfixResults), oddLetterResults=oddLetterResults, oddLetterCount=len(oddLetterResults),
                           lackingVowelResults=lackingVowelResults, lackingVowelCount=len(lackingVowelResults))
