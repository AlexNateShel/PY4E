# Python For Everyboy Chapter 10 Exercise 2

# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04  3
# 06  1
# 07  1
# 09  2
# 10  3
# 11  6
# 14  1
# 15  2
# 16  4
# 17  2
# 18  1
# 19  1

fname = input('Enter a file name: ')
fhand = open(fname)
dict1 = {}

for line in fhand:
    if line.startswith('From '):
        line = line.split(' ')
        time = line[6]
        hour = time[:2]
        if hour not in dict1:
            dict1[hour] = 1
        else:
            dict1[hour] += 1

sorted_dict = dict(sorted((key, value) for (key, value) in dict1.items()))
for x, y in sorted_dict.items():
    print(x, y)