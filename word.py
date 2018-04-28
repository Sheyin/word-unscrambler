# List of prefixes/postfixes to check against

postfixes = ["ach", "ack", "act", "age", "aid", "aim", "ain", "air", "ame", "and", "ane", "ang", "ant",
            "arg", "arn", "art", "atch", "ave",
            "eep", "egg", "erg",
            "ign", "ion", "ity",
            "nge", "nut",
            "old", "ome" "ood", "ore", "ough", "our", "ous", "out",
            "pen", "ple",
            "rge", "rin", "rve",
            "ten", "thin", "tic", "tin", "tion"
            "ag", "al", "an", "ar", "at", "ay",
            "ce", "de",
            "ea", "ed", "ee", "em", "en", "er", "es", "et", "ey",
            "ft",
            "id", "il", "im", "in", "ip", "it",
            "ld", "le", "ll", "ly",
            "me", "ne", "ng", "nt",
            "oc", "og", "ol", "op", "or", "ot",
            "rd", "re", "rl", "ry", "se", "sh", "ss", "st", "te", "un", "ur", "us", "vy", "ye"]

# This system should really be combined into vowel + consonant pairings, so ex. -rl is only valid if it has a vowel before it

# Removed due to duplication:
# ase, ese, etc

# There is a lot of overlap, especially with 2 and 3 letter postfixes
# ex. -te and -ate

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
specialConstantPairs = ['st', 'ch', 'chr', 'nt', 'gh', 'fr', 'pr', 'wh', 'pl', 'ly', 'ty', 'ry', 'rd', 'br', 'mp']

# Think about letter pairs that will never be matched -> regular expression
# ex. mc, gp, dp, qc, etc. should be filtered in an expression
