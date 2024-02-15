# Python For Everybody Chapter 10 Exercise 1

# Revice a previos program as follows: Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dicionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From  stephen.marquard@uct.ac.za  Sat  Jan   5  09:14:16  2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqaian@umich.edu 195

fname = input('Enter a file name: ')
fhand = open(fname)
dict1 = {}
list1 = []

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        email = line[1]
        if email not in dict1:
            dict1[email] = 1
        else:
            dict1[email] += 1

for k, v in dict1.items():
    tuple1 = (v, k)
    list1.append(tuple1)

list1.sort(reverse=True)
print(list1[0])