# Function that removes given letters from subset and prints probable combinations
import math
from copy import copy
import itertools

# Letters: the pool of letters to choose from
# Subset: a detected combination of letters to exclude from the pool and build combinations upon
def unscramble(letters, subset, type):
    #print("Debug: letters is: " + str(letters) + ", subset: " + str(subset) + ", type: " + type)
    # Remove the first instance of each letter from the pool
    for character in subset:
        letters.remove(character)

    # Create combinations based on remaining letters and adding postfix
    print("There are " + str(len(letters)) + " letters remaining, - " + str(math.factorial(len(letters))) + " - combinations possible.")

    remainingLetters = copy(letters)
    result = itertools.permutations(letters)
    # This returns tuples
    for permutation in result:
        combination = ''.join(permutation) + subset
        print(combination)


def checkDuplicateLetters(letters, subset):
    for _ in subset:
        try:
            letters.remove(_)
        except ValueError:
            return False
    else:
        return True
    # Any errors?
