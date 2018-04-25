# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools

# Letters: the pool of letters to choose from
# Subset: a detected combination of letters to exclude from the pool and build combinations upon
def unscramble(letters, subset, type, spaces):
    #remainingLetters = copy(letters)
    numLettersToRemove = len(letters) - spaces
    #print("Debug: letters is: " + str(letters) + ", subset: " + str(subset) + ", type: " + type)
    # Remove the first instance of each letter from the pool
    for character in subset:
        letters.remove(character)

    # Create combinations based on remaining letters and adding postfix
    # This math only works for spaces = letters
    print("There are " + str(len(letters)) + " letters remaining, - " + str(math.factorial(len(letters))) + " - combinations possible.")


    result = itertools.permutations(letters)
    #print("numLettersToRemove: " + str(numLettersToRemove))
    # This returns tuples
    # TODO: If duplicates after a truncate, should probably remove from list
    # TODO: Add method for inputting known letter positions, if it invalidates a prefix, skip processing
    results = []
    for permutation in result:
        combination = ''.join(permutation) + subset
        combination = combination[numLettersToRemove:]
        if combination not in results:
            results.append(combination)
        #print(combination)
    # Print results here or in main?
    for _ in results:
        print(_)


def checkDuplicateLetters(letters, subset):
    for _ in subset:
        try:
            letters.remove(_)
        except ValueError:
            return False
    else:
        return True
    # Any errors?
