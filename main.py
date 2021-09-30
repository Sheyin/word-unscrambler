# The goal is to create a list of word-patterns based on certain letter combinations in the English language.
# Source: https://github.com/Sheyin/word-unscrambler

from functions import invalidInput, formatInput, generateCombinations
import dictionary
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def start():
    return render_template('index.html', title="Search for a word")


# This section is customized for the original word search only
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

    postfixResults.sort()
    nonPostfixResults.sort()
    oddLetterResults.sort()
    lackingVowelResults.sort()

    # See if anything in the postfix results matches a word in the database.
    # This might be buggy as it does not always have plurals, slang, etc.
    # Also, lag.  I hope the server forgives me.
    confirmed_words = dictionary.lookup(postfixResults)

    totalCount = len(postfixResults) + len(nonPostfixResults) + \
        len(oddLetterResults) + len(lackingVowelResults)

    return render_template('results.html', title="Results for '" + ''.join(letters) + "'", letters=''.join(letters), totalCount=totalCount, postfixResults=postfixResults, postfixCount=len(postfixResults),
                           nonPostfixResults=nonPostfixResults, nonPostfixCount=len(nonPostfixResults), oddLetterResults=oddLetterResults, oddLetterCount=len(oddLetterResults),
                           lackingVowelResults=lackingVowelResults, lackingVowelCount=len(lackingVowelResults), confirmedResults=confirmed_words, confirmedCount=len(confirmed_words))


# This will perform the lookup to get around the old dictionary/hosting problem
# Expects 4 parameters: the letter scramble, length of the word (optional), any known letters (optional), what those known letters are (optional)
# todo - abstract this function away from lookup / gamelookup and turn /lookup into a simple api endpoint
# Expects a json request with the data (if available)
@app.route('/gamelookup', methods=['GET'])
def gamelookup():

    inputReceived = request.args.get()
    lettersInput = request.args.get('letters', '')
    numSpacesInput = request.args.get('length', '')
    knownInput = request.args.get('known', '')
    knownLettersInput = request.args.get('knownLetters', '')

    # Leaving this in for debug reasons
    print("Received: ")
    print("Letters: " + lettersInput + " numSpaces: " + numSpacesInput +
          " knownInput: " + knownInput + " knownLettersInput: " + knownLettersInput)

    invalid, invalidReason = invalidInput(
        lettersInput, numSpacesInput, knownInput, knownLettersInput)
    if invalid:
        # Response should contain the error, logic in page template will determine what is shown
        response = {"error": True, "reason": invalidReason}
        return json.dumps(result)
        # return render_template('error.html', title="Error!", reason=invalidReason)

    # Only do these after input has been checked
    letters, numSpaces, known, knownLetters = formatInput(
        lettersInput, knownInput, numSpacesInput, knownLettersInput)
    print("After formatting:")
    print("Letters: " + str(letters) + " numSpaces: " + str(numSpaces) +
          " known: " + str(known) + " knownLetters: " + str(knownLetters))
    postfixResults, nonPostfixResults, oddLetterResults, lackingVowelResults = generateCombinations(
        letters, numSpaces, known, knownLetters)

    postfixResults.sort()
    nonPostfixResults.sort()
    oddLetterResults.sort()
    lackingVowelResults.sort()

    # See if anything in the postfix results matches a word in the database.
    # This might be buggy as it does not always have plurals, slang, etc.
    # Also, lag.  I hope the server forgives me.
    confirmed_words = dictionary.lookup(postfixResults)

    # totalCount = len(postfixResults) + len(nonPostfixResults) + \
    # len(oddLetterResults) + len(lackingVowelResults)

    result = {
        "error": False,
        "reason": "",
        "postfixResults": postfixResults,
        "nonPostfixResults": nonPostfixResults,
        "oddLetterResults": oddLetterResults,
        "lackingVowelResults": lackingVowelResults,
        "confirmedResults": confirmed_words,
    }

    return json.dumps(result)
