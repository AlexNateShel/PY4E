# Write a program that prompts for a file name, then opens that file and reads through the file, and print the conents of the file in upper case. 
# Use the file 'words.txt' to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name

fname = input('Please enter a file name: ')
fh = open(fname)
txt = fh.read()
shout = txt.rstrip()
print(shout.upper())
