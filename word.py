# List of prefixes/postfixes to check against

postfixes = ["act", "alpha",
            "che",
            "eek", "eep", "egg", "ewd",
			"ght",
            "ign", "ism", "ity", "kappa", "kiwi", "lambda",
            "ood", "ook", "ough", "oul",
            "the", "thy",
            "ab", "ad", "ag", "al", "am", "an", "ap", "ar", "at", "ay",
            "be",
            "ce", "ch", "ck", "cy", "de", "do",
            "ea", "ed", "ee", "ef", "el", "em", "en", "er", "es", "et", "ew", "ey",
            "ff", "ft", "ga", "ge", "go", "hi", "io",
            "ic", "id", "ie", "il", "im", "in", "ip", "ir", "it", "ke",
            "la", "ld", "le", "lk", "ll", "lm", "lo", "lt", "ly",
            "ma", "mb", "me", "mp", "na", "nd", "ne", "ng", "nk", "nt", "ny",
            "oc", "od", "oe", "og", "ol", "om", "on", "oo", "op", "or", "ot", "ow", "ox",
            "py",
            "ra", "rb", "rd", "re", "rg", "rl", "rn", "ro", "ry", "rt",
			"se", "sh", "ss", "st", "sy",
			"ta", "te", "th", "ty",
			"ub", "ud", "ue", "um", "un", "up", "ur", "us", "ut",
			"ve", "vy", "we", "wl", "ye"]



# Allowed to start with any vowel, or vowel + consonant
# Or any constant + c, r, l, h, y, t, in second space
softConsonants = ['c', 'h', 'l', 'n', 'r', 's', 't', 'w', 'y']
hardConsonants = ['b', 'd', 'f', 'g', 'j', 'k', 'm', 'n', 'p', 'q', 'v', 'x', 'z']
startWithExceptions = ['kn', 'ps', 'sp']
softConsonantPairsLegal = ['ch', 'cl', 'cr', 'cy', 'rh', 'ry', 'sc', 'sh', 'sl', 'sn', 'st', 'sw', 'th', 'tr', 'tw', 'ty', 'wh', 'wr']
#legalStartingVowelPairings = ["aa", "ai", "au", "ea", "ee", "eo", "eu", "oa", "oi", "oo", "ou"]
# Adding in a few -h ones as well - may as well since it is the same check
illegalStartingVowelPairings = ["ae", "ao", "eh", "ei", "eo", "ia", "ie", "ih", "ii", "io", "iu", "oe", "oh", "ua", "ue", "uh", "ui", "uo", "uu"]

# TODO: There should be an exception list for greek letters since they aren't really postfixes but show up commonly.
# They would also only be exact matches, never partial. ex. alpha, lambda, tau, etc.

# This system should really be combined into vowel + consonant pairings, so ex. -rl is only valid if it has a vowel before it

# There is a lot of overlap, especially with 2 and 3 letter postfixes
# ex. -te and -ate

# The following is not used yet, but is something I am thinking on to improve on filtering junk.
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
vowelExceptions = ['chr', 'cry', 'cyc', 'thr', 'thy', 'tyc', 'tyk', 'tyr']
#slag, snag, knee - 4 letter words being mistakenly filtered.  Maybe make an exception to the rule?


# Some removed pairings that aren't really used for the start of words.
# nt, ly, ty, rd, mp
# This is inefficient but compiling this data will give me a better idea of a more general rule.
# Current rule: if 1st letter is not in hardConsonants, and 2nd letter is in softConsonants, then it is allowed
# Seems like they just have to be illegal combinations of softConsonants at this point
neverStartWith = ['cs', 'ct', 'cw', 'sr', 'tc', 'tl',
			]

# Think about letter pairs that will never be matched -> regular expression
# ex. mc, gp, dp, qc, etc. should be filtered in an expression
# Somewhat common pairs - ll, oo, ee, mm, zz
