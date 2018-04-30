# List of prefixes/postfixes to check against

postfixes = ["ach", "ack", "act", "acy", "age", "aid", "aim", "ain", "air", "ame", "and", "ane", "ang", "ant",
            "arg", "arn", "art", "atch", "ave", "che", "cle",
            "eep", "egg", "erg",
            "ign", "ion", "ity",
            "nge", "nut", "ncy",
            "old", "ome" "ood", "ook", "ore", "ough", "our", "ous", "out",
            "pen", "ple",
            "rge", "rin", "rve",
            "ten", "the", "thin", "tic", "tin", "tion", "uff", "val", "vel",
            "ag", "al", "am", "an", "ap", "ar", "at", "ay",
            "be",
            "ce", "ch", "ck", "de",
            "ea", "ed", "ee", "ef", "el", "em", "en", "er", "es", "et", "ew", "ey",
            "ft", "ga", "ge", "go",
            "ic", "id", "ie", "il", "im", "in", "ip", "it",
            "ld", "le", "lk", "ll", "lo", "lt", "ly",
            "mb", "me", "mp", "nd", "ne", "ng", "nk", "nt", "ny",
            "oc", "oe", "og", "ol", "om", "on", "oo", "op", "or", "ot", "ow", "ox",
            "py",
            "rd", "re", "rl", "ry", "se", "sh", "ss", "st", "te", "th", "ty", "ub", "ue", "um", "un", "up", "ur", "us", "ut", "ve", "vy", "ye"]

# This system should really be combined into vowel + consonant pairings, so ex. -rl is only valid if it has a vowel before it

# There is a lot of overlap, especially with 2 and 3 letter postfixes
# ex. -te and -ate

# The following is not used yet, but is something I am thinking on to improve on filtering junk.
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
specialConstantPairs = ['st', 'ch', 'chr', 'nt', 'gh', 'fr', 'pr', 'wh', 'pl', 'ly', 'ty', 'ry', 'rd', 'br', 'mp']

# Think about letter pairs that will never be matched -> regular expression
# ex. mc, gp, dp, qc, etc. should be filtered in an expression
