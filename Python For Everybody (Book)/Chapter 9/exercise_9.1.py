# Python For Everybody Chapter 9 Exercise 1

# Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in *words.txt* and stores them as keys in a dictionary. 
# It doesn't matter what the values are. 
# Then you can use the *in* operator as a fast way to check whether a string is in the dictionary.


word = input('Please enter a string to check whether it is in the file : ')
words = dict()
fname = 'words.txt'
for x in fname:
    if x not in words:
        words[x] = 1
    else:
        words[x] = words[x] + 1

print(word, 'is in the file', words[x], 'times.')