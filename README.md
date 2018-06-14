# word-unscrambler

I started writing this up when I was stumped playing "WordScapes" on iOS.  The premise of that game is that you have a pool of letters to unscramble and form words that fit on a crossword grid.  However, one of the things that frustrated me is that it does not follow "Scrabble rules" - ie. some abbreviations/slang is allowed, etc.  So simply matching up words against a dictionary might not work as well, though I'm sure one exists that would go through this process in a more logical manner.

This program basically goes through and performs the actions I go through in my head.  I go through a mental list of common word patterns, and if there is one that is found in the given letters, then I make some permutations to mentally pronounce the word and see if it might be the one in question.  Even though this is effectively brute forcing combinations, it is still limited by the list of postfixes I added.  Plus, writing this up somehow makes me feel like this isn't quite cheating.

Currently, this algorithm is not intelligent - it simply searches through patterns I have entered and prints a list.  I hope to improve on this (and hopefully find the answer to the word(s) I'm stuck on in the process).  It sort of works, but struggles with some of the more unique word combinations / ones I haven't thought of yet.  A major problem is that it currently lacks a method of filtering junk from the results, so it is easy to overlook a word that it has discovered.

Current working features:
- (some) Postfixes
- Basic matching and permutations
- Generates words that are composed of less than the maximum amount of letters
- Limiting words based on known letter positions
- (some) handling of plurals

Things to add:
- Improving algorithm - right now it is not precisely efficient
- Intelligent filtering of less likely letter combinations
- More combinations (mostly focusing on adding postfixes, some may have been overlooked)

Bugs:
- Work on filtering duplicates

Usage:
<b>python main.py</b> runs the console-only version.

The other method requires <a href="http://flask.pocoo.org/">installing Flask</a>, setting FLASK_APP to <b>main_flask.py</b>, then running flask by entering <b>flask run</b>. (This is the preferred route; it is much easier to use than the console-only interface.)
