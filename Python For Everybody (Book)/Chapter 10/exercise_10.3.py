# Python For Everybody Chapter 10 Exercise 3

# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should vonvert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anythin other than the letters a-z.
# Find text samples from several different locations and see how letter frequency varies between languages. 
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

fname = input('Enter a file name: ')
fhand = open(fname)
letters= {}
srt = {}

for line in fhand:
    line = line.split(' ')
    for word in line:
        for letter in word:
            if letter.isalpha():
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1
            else: continue

sorted_letters = dict(sorted((value, key) for (key, value) in letters.items()))
for k, v in reversed(sorted_letters.items()):
    print(v, k)
