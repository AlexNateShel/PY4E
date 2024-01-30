# Python For Everybody Chapter 9 Exercise 4

# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop to find who has the most messages and print out how many messages the person has.

fname = input('Please enter a filename: ')
fhand = open(fname)
email = {}

for line in fhand:
    if line.startswith('From '):
        address = line.split()[1]
        email[address] = email.get(address, 0) + 1

max_address = None
max_emails = 0
for x in email:
    if email[x] > max_emails:
        max_address = x
        max_emails = email[x]

print(max_address, max_emails)
