# Python For Everybody Chapter 11 Exercise 1

# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

# python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

import re

fname = input('Enter the filename: ')
regex = input('Enter a regular expression: ')

count = 0
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1

print(fname, 'had', count, 'lines that matched', regex)
