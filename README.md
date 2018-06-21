# word-unscrambler

Currently hosted <a href="http://sheyin.pythonanywhere.com/">here</a>.

I started writing this up when I was stumped playing "WordScapes" on iOS.  The premise of that game is that you have a pool of letters to unscramble and form words that fit on a crossword grid.  However, one of the things that frustrated me is that it does not follow "Scrabble rules" - ie. some abbreviations/slang is allowed, etc.  So simply matching up words against a dictionary might not work as well, though I'm sure one exists that would go through this process in a more logical manner.

This program basically goes through and performs the actions I go through in my head.  I go through a mental list of common word patterns, and if there is one that is found in the given letters, then I make some permutations to mentally pronounce the word and see if it might be the one in question.  Even though this is effectively brute forcing combinations, it is still limited by the list of postfixes I added.  Plus, writing this up somehow makes me feel like this isn't quite cheating.

Currently, this algorithm is not intelligent - it simply searches through patterns I have entered and prints a list.  I hope to improve on this (and hopefully find the answer to the word(s) I'm stuck on in the process).  It sort of works, but struggles with some of the more unique word combinations / ones I haven't thought of yet.  A major problem is that it currently lacks a method of filtering junk from the results, so it is easy to overlook a word that it has discovered.

Features:
- Calculates combinations of letters, currently only if it matches a specified postfix
- Filters some junk results based on lack of vowels, unusual starting letters
- Performs input validation and returns error messages

Things to add:
- Improving algorithm (debating on how at this point)

Bugs:
- Fixed the ones I know about - let me know if you find more!

Usage:
It is currently hosted <a href="http://sheyin.pythonanywhere.com/">here</a>.

To run it yourself, <a href="http://flask.pocoo.org/">Flask</a> needs to be installed.  On Windows, set FLASK_APP to <b>main.py</b>, then running flask by entering <b>flask run</b>.

Screenshots:  
<img src="screenshots/screenshot1.jpg" alt="Entering info about the word">  
<img src="screenshots/screenshot2.jpg" alt="Results found by the program">  
