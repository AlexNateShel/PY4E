# Python For Everybody Chapter 9 Exercise 3

# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

fname = input('Please enter a filename: ')
fhand = open(fname)
email = {}

for line in fhand:
    if line.startswith('From '):
        address = line.split()[1]
        email[address] = email.get(address, 0) + 1

print(email)
