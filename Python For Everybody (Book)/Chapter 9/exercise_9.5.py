# Python For Everybody Chapter 9 Exercise 5

# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fname = input('Please enter a filename: ')
fhand = open(fname)
domains = {}

for line in fhand:
    if line.startswith('From '):
        address  = line.split()[1]
        domain = address.split('@')[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)