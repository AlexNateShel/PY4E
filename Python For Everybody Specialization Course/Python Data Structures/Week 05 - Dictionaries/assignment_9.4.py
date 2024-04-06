# Write a program to read through the 'mbox-short.txt' and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From' lines and takes the second word of those lines as the person who sent the email.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname = 'mbox-short.txt'
fhand = open(fname)

sender = dict()
for lines in fhand:
    if not lines.startswith('From:'): continue
    lines = lines.split()
    lines = lines[1]
    sender[lines] = sender.get(lines, 0) + 1

big_comment = None
big_num = None
for comment, num in sender.items():
    if big_num is None or num > big_num:
        big_comment = comment
        big_num = num

print(big_comment, big_num)