# List of prefixes/postfixes to check against

postfixes = ["act", "alpha",
            "che",
            "eek", "eep", "egg", "ewd",
			"ght",
            "ign", "ism", "ity", "kappa", "lambda",
            "ood", "ook", "ough", "oul",
            "the", "thy",
            "ab", "ad", "ag", "al", "am", "an", "ap", "ar", "at", "ay",
            "be",
            "ce", "ch", "ck", "cy", "de",
            "ea", "ed", "ee", "ef", "el", "em", "en", "er", "es", "et", "ew", "ey",
            "ff", "ft", "ga", "ge", "go", "hi",
            "ic", "id", "ie", "il", "im", "in", "ip", "ir", "it",
            "la", "ld", "le", "lk", "ll", "lo", "lt", "ly",
            "ma", "mb", "me", "mp", "na", "nd", "ne", "ng", "nk", "nt", "ny",
            "oc", "oe", "og", "ol", "om", "on", "oo", "op", "or", "ot", "ow", "ox",
            "py",
            "ra", "rd", "re", "rg", "rl", "rn", "ry", "rt",
			"se", "sh", "ss", "st", "sy",
			"ta", "te", "th", "ty",
			"ub", "ue", "um", "un", "up", "ur", "us", "ut",
			"ve", "vy", "we", "ye"]

# TODO: There should be an exception list for greek letters since they aren't really postfixes but show up commonly.
# They would also only be exact matches, never partial. ex. alpha, lambda, tau, etc.

# This system should really be combined into vowel + consonant pairings, so ex. -rl is only valid if it has a vowel before it

# There is a lot of overlap, especially with 2 and 3 letter postfixes
# ex. -te and -ate

# The following is not used yet, but is something I am thinking on to improve on filtering junk.
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
vowelExceptions = ['chr', 'thr', 'thy', 'tyc', 'tyk', 'tyr']
#slag, snag, knee - 4 letter words being mistakenly filtered.  Maybe make an exception to the rule?
specialConsonantPairs = ['bl', 'br', 'ch', 'cl', 'cr', 'cy', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'hy', 'kn', 'll', 'my',
						'ph', 'kn', 'ph', 'pl', 'pr', 'py', 'rh', 'ry', 'sc', 'sh', 'st', 'th', 'tr', 'wh', 'wr']

# Some removed pairings that aren't really used for the start of words.
# nt, ly, ty, rd, mp

# Think about letter pairs that will never be matched -> regular expression
# ex. mc, gp, dp, qc, etc. should be filtered in an expression
# Somewhat common pairs - ll, oo, ee, mm, zz
