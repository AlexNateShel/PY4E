# Python For Everybody (Book) (PY4E)

## Chapter 7: Files Exercises

### Exercise 1. Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
###  You can download the sample data at http://www.py4e.com/code3/words.txt
```
fname = input('Please enter a file name: ')
fh = open(fname)
txt = fh.read()
shout = txt.rstrip()
print(shout.upper())
```

### Exercise 2.  Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
```
 X-DSPAM-Confidence:   0.8475
```
### When you encounter a line that starts with "X-DSPAM-Confidence:" pullt apart the line to extract the floating-point number on the line. Count these lines and then compute the total number of spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
```
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

count = 0
total = 0
fname = input('Please enter a file name: ')
fh = open(fname)
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count += 1
        a = line.find('0')
        x = line[a:]
        total = total + float(x)
        
average = total / count
print('Average spam confidence: ', average)
```

### Exercise 3. Sometimes when programmers get bored or want to have a bit of fun, they add a harmless *Easter Egg* to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo". The program should behave normally for all other files which exist and don't exist. Here is a sample execution of the program:
```
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.txt
File cannot be opened: missing.txt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!


fname = input('Please enter a file name: ')
try:
    if fname == 'na na boo boo' :
        print("You've been punk'd")
        exit()
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ' fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1

print('There were', count, 'subject lines in', fname)
```
