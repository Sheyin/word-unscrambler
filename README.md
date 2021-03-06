# word-unscrambler

I started writing this up when I was stumped playing "WordScapes" on iOS. The premise of that game is that you have a pool of letters to unscramble and form words that fit on a crossword grid. However, one of the things that frustrated me is that it does not follow "Scrabble rules" - ie. some abbreviations/slang is allowed, etc. So simply matching up words against a dictionary might not work as well, though I'm sure one exists that would go through this process in a more logical manner.

This has been redesigned to list all possible combinations, and remove results based on certain criteria. I began by making a list of common word patterns and eliminating the results that did not fit this criteria. However, it was a bit too broad, and I was forced to add a number of exclusions that made the "possible results" very cluttered with nonsense words. Eventually, I added a check to query a database to see if it is a legal word, but since I am not quite sure how comprehensive the database is, I elected to display all the possible results in different sections to allow the user to search through them if the program failed to find a word.

Features:

- Determines all combinations of letters and filters junk ones based on lack of vowels, unusual starting letters, duplicate entries
- Checks results against a dictionary (database of words) to return primarily correct words, if found
- Performs input validation and warns the user when appropriate
- Mobile-responsive - should be easy to use on either desktop or mobile device

Things to add:

- Improving algorithm to remove more junk results / speed up search time

Bugs:

- Fixed the ones I know about - let me know if you find more!
- Live version stopped working abruptly and I'm not quite sure why (database issues). Planning to rebuild to handle this differently.

Usage:
Removed link to live hosted site temporarily since it something has gone wrong, and I'd like to rebuild this project differently than before.

Screenshots:
<br /><img src="screenshots/screenshot3.jpg" alt="Filling out information about the word">  
<br /><img src="screenshots/screenshot4.jpg" alt="Results found by the application">
