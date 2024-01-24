# Chapter 7 PY4E Quiz

### 1. Given the architecture and terminology we introduced in Chapter 1, where are files stored?
- [x] Secondary memory
- [ ] Central Processor
- [ ] Motherboard
- [ ] Main Memory

### 2. What is stored in a "file handle" that is returned from a successful __open()__ call?  
- [ ] The handle has a list of all of the files in a particular folder on the hard drive
- [x] The handle is a connection to the file's data
- [ ] The handle contains the first 10 lines of a file
- [ ] All the data from the file is read into memory and stored in the handle

### 3. What do we use the second parameter of the __open()__ call to indicate?   
- [ ] What disk drive the file is stored on
- [x] Whether we want to read data from the file or write data to the file
- [ ] How large we expect the file to be
- [ ] The list of folders to be searched to find the file we want to open

### 4. What Python function would you use if you wanted to prompt the user for a file name to open?   
- [x] input()
- [ ] file_input()
- [ ] gets()
- [ ] alert()

### 5. What is the purpose of the newline character in text files?  
- [ ] It allows us to open more than one files and read them in a synchronized manner
- [x] It indicates the end of one line of text and the beginning of another line of text
- [ ] It enables random movement throughout the file
- [ ] It adds a new network connection to retrieve files from the network

### 6. If we open a file as follows:
```
xfile = open('mbox.txt')
```
### What statement would we use to read the file one line at a time?
- [ ] READ (xfile,*,END=10) line
- [x] for line in xfile:
- [ ] while ( getline (xfile,line) ) {
- [ ] while (<xfile>) {

### 7. What is the purpose of the following Python code?
```
fhand = open('mbox.txt')
x = 0
for line in fhand:
    x = x + 1
print(x)
```
- [x] Count the lines in the file 'mbox.txt'
- [ ] Convert the lines in 'mbox.txt' to uppercase
- [ ] Reverse the order of the lines in 'mbox.txt'
- [ ] Remove the leading and trailing spaces from each line in 'mbox.txt'

### 8. If you write a Python program to read a text file and you see extra blank lines in the output that are not present in the file input as showm below, what Python string function will likely solve the problem?
```
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu
```  
- [ ] ljust() 
- [ ] startswith()
- [x] rstrip()
- [ ] trim()

### 9. The following code sequence fails with a traceback when the user enters a file that does not exist. How would you avoid the traceback and make it so you could print out your own message when a bad file name was entered? 
- [ ] begin / rescue / end
- [x] try / except
- [ ] setjmp / longjmp
- [ ] on error resume next

### 10. What does the following Python code do?
```
fhand = open('mbox-short.txt')
inp = fhand.read()
```  
- [ ] Checks to see if the file exists and can be written
- [ ] Turns the text in the file into a graphic image like a PNG or JPG
- [x] reads the entire file into the variable __inp__ as a string
- [ ] Prompts the user for a file name
