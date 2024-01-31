# Write a program to read through the 'mbox-short.txt' and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquad@uct.ac.za  Sat  Jan   5  09:14:16  2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by the hour.

dts = dict()
hrs = dict()
fname = input('Enter a file name: ')

if len(fname) < 1 : 
    fname = 'mbox-short.txt'

fhand = open(fname)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        dt = line[5]
        hrs = dt[0:2]
        dts[hrs] = dts.get(hrs, 0) + 1

for k, v in sorted(dts.items()):
    print(k, v)

