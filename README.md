# word-unscrambler

I started writing this up when I was stumped playing "WordScapes" on iOS.  The premise of that game is that you have a pool of letters to unscramble and form words that fit on a crossword grid.  However, one of the things that frustrated me is that it does not follow "Scrabble rules" - ie, some abbreviations/slang is allowed, some words that seemingly make no sense to include in a dictionary, etc.  So simply matching up words against a dictionary might not work, although the game does list its sources for each word (after discovery).

This program basically goes through and performs the actions I go through in my head.  I go through a mental list of common word patterns, and if there is one that is found in the given letters, then I make some permutations to mentally pronounce the word and see if it might be the one in question.

Currently, this algorithm is not intelligent - it simply searches through patterns I have entered and prints a list.  I hope to improve on this (and hopefully find the answer to the word(s) I'm stuck on in the process).  It sort of works, but struggles with some of the more unique word combinations / ones I haven't thought of yet.

Current working features:
- (some) Postfixes
- Basic matching and permutations
- Generates words that are composed of less than the maximum amount of letters

Things to add:
- Limiting words based on known letter positions
- Searching for prefixes, mid-word-patterns
- Handling of plurals, -er, -est postfixes
- Intelligent filtering of less likely letter combinations
