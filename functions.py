# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools

# Letters: the pool of letters to choose from
# Subset: a detected combination of letters to exclude from the pool and build combinations upon
def unscramble(letters, subset, type, spaces, solutions):
    #remainingLetters = copy(letters)
    numLettersToRemove = len(letters) - spaces
    solution = []
    # Remove the first instance of each letter of subset from the pool
    for character in subset:
        letters.remove(character)
    # if there is an s, and it is not part of the sunset, then temporarily remove
    # it from the letter pool, reduce the total space by one, and readd it after the postfix.
    # This should also be done in addition to keeping the s in the word pool, effectively doubling the process?

    # If there is only 1 s, and it is being used in the subset, then skip the plural
    # AND make sure it obeys the # of spaces requested
    if ('s' not in subset and letters.count('s') >= 1) or ('s' in subset and letters.count('s') >= 2):
        #print("Plural Handling Start")
        pluralLetters = copy(letters)
        pluralLetters.remove('s')
        pluralResults = itertools.permutations(pluralLetters)

        for pluralPermutation in pluralResults:
            pluralCombination = ''.join(pluralPermutation) + subset
            pluralCombination = pluralCombination[numLettersToRemove:]
            pluralCombination += 's'
            #print("Raw plural combination: " + pluralCombination)
            if pluralCombination not in solution and pluralCombination not in solutions:
                solution.append(pluralCombination)


    results = itertools.permutations(letters)
    # TODO: Add method for inputting known letter positions, if it invalidates a prefix, skip processing

    for permutation in results:
        combination = ''.join(permutation) + subset
        combination = combination[numLettersToRemove:]
        if combination not in solution:
            solution.append(combination)

    return solution


def checkDuplicateLetters(letters, subset):
    for _ in subset:
        try:
            letters.remove(_)
        except ValueError:
            return False
    else:
        return True
    # Any errors?


# Keeps only the words that match a letter in the position of a known letter
def filterKnownLetters(solutions, letterPairings):
    filteredSolutions = []
    # This needs to be rerun if more than 1 known letter, because some matches will include ones invalidated by other matches
    for _ in range(0, len(letterPairings)):
        for letter, position in letterPairings:
            print("Debug: running checkValidCombo on letter: " + letter + " position: " + str(position))
            filteredSolutions += checkValidCombo(solutions, letter, position)
    return filteredSolutions


def checkValidCombo(solutions, letter, position):
    tempSolutions = []
    for word in solutions:
        if word[position] == letter:
            tempSolutions.append(word)
    return tempSolutions


# Returns a list of tuples of a letter and position
def matchLetterPosition(knownLetters):
    positions = []
    for position in range(0, len(knownLetters)):
        if knownLetters[position] not in ['', ' ']:
            positions.append((knownLetters[position], position))
            #print("Added: " + str((knownLetters[position], position)))
    return positions


# Simply prints text indented a bit for easier reading.
def printIndented(text):
    print("   " + text)
