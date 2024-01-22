# Python For Everybody Chapter 1 Exercises

### Exercise 1: What is the function of the secondary memory in a computer?
- [ ] Execute all of the computation and logic of the program
- [ ] Retrieve web pages over the internet
- [x] Store information for the long term, even beyond a power cycle
- [ ] Take input from the user

### Exercise 2: What is a program?
- A program is a set of instructions that specify computations

### Exercise 3: What is the difference between a compiler and an interpreter?
- A compiler translates a program written in a high-level language into a low-level language all at once, in preparation for later executions. An interpret executes a program in a high-level language by translating it one line at a time.

### Exercise 4: Which of the following contains "machine code"?
- [ ] The Python interpreter
- [ ] The keyboard
- [x] Python source file
- [ ] A word processing document

### Exercise 5: What is wrong with the following code:
```
>>> primt 'Hello world!'
File "<stdin>", line 1
    primt 'Hello world!'

SyntaxError: invalid syntax
>>>
```
- The print function is misspelled and is also missing the parentheses ().

### Exercise 6: Where in the computer is a variable such as "x" stored after the following Python line finishes?
```
x = 123
```
- [ ] Central processing unit
- [x] Main Memory
- [ ] Secondary Memory
- [ ] Input Devices
- [ ] Output Devices

### Exercise 7: What will the following program print out:
```
x = 43
x = x - 1
print(x)
```
- [ ] 43
- [x] 42
- [ ] x + 1
- [ ] Error because x = x + 1 is not possible mathematically

### Exercise 8: Explain each of the following using an example of a human capability: 
#### (1) Central Processing Unit
The human equivalent to the Central Processing Unit is the brain.

#### (2) Main Memory
The human equivalent to Main Memory is short term memory.

#### (3) Seconday Memory
The human equivalent to Secondary Memory is long term memory.

#### (4) Input Device 
The human equivalent to an input device is the ears and eyes.

#### (5) Output Device
The human equivalent to a output device is our mouths/voices.

### Exercise 9: How do you fix a "Syntax Error"? 
Find the "grammar" rules that have been violated, the incorrect syntax that is causing the error, and correct it. Python usually points to where the error is occuring, but sometimes the mistake was earlier in the program than when Python noticed it. 