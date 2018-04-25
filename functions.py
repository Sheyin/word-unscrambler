# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools

# Letters: the pool of letters to choose from
# Subset: a detected combination of letters to exclude from the pool and build combinations upon
def unscramble(letters, subset, type):
    print("Debug: letters is: " + str(letters) + ", subset: " + str(subset) + ", type: " + type)
    # Remove the first instance of each letter from the pool
    for character in subset:
        print("Debug: character: " + character)
        letters.remove(character)
    #remainingLetters = letters
    print("Debug: Remaining letters: " + str(letters))

    # Create combinations based on remaining letters and adding postfix
    print("There are " + str(len(letters)) + " letters remaining, - " + str(math.factorial(len(letters))) + " - combinations possible.")


    remainingLetters = copy(letters)
    result = itertools.permutations(letters)
    # This returns tuples
    for permutation in result:
        print("Debug: " + str(permutation))
        combination = ''.join(permutation) + subset
        print(combination)

    '''
    while len(remainingLetters) > 0:
        #print("Looking at: " + character)
        result = combine(copy(letters), copy(poppedLetters))
        poppedLetters = remainingLetters.pop(0)
        print("Result: " + result)
    '''





'''
def combine(letters, poppedLetters):
    result = ""
    if len(letters) > 1:
        result += letters.pop()
        #print("Combo: " + result)
        result += combine(letters)
        return result
    else:
        return letters.pop()
'''
'''
    totalLetters = copy(remainingLetters)
    letters = remainingLetters
    possibleCombinations = math.factorial(len(remainingLetters))
    foundCombinations = []

    while len(lettersChecked < len(remainingLetters)):
        lettersChecked = []
        firstLetter = remainingLetters.pop()
        lettersEliminated.append(firstLetter)
        lettersChecked.append(firstLetter)
        combo.append(firstLetter)

    firstLetter = remainingLetters.pop()
    lettersChecked.append(firstLetter)


# Making combination function recursive
def removeLetter(letters):
    pass
'''
