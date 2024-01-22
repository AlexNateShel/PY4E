# Chapter 4 Quiz PY4E - Python For Everybody 

### 1. Which Python keyword indicates the start of a function definition?
- [x] def
- [ ] help
- [ ] continue
- [ ] sweet

### 2. In Python, how do you indicate the end of the block of code that makes up the function?  
- [ ] You add the matching curly brace that was used to start the function }
- [x] You de-indent a line of code to the same indent level as the __def__ keyword
- [ ] You put the "END" keyword in column 7 of the line which is to be the last line of the function
- [ ] You put a # character at the end of the last line of the function

### 3. In Python what is the __input()__ feature best described as?   
- [ ] A user-defined function
- [ ] The central processing unit
- [x] A built-in function
- [ ] A conditional statement

### 4. What does the following code print out?
```
def thing():
    print('Hello')

print('There')
```   
- [ ] thing
      Hello
      There
- [ ] def
      thing
- [x] There
- [ ] thing

### 5. In the following Python code, which of the following is and "arguement" to a function?
```
x = 'banana'
y = max(x)
z = y * 2
```  
- [x] x
- [ ] max
- [ ] 'banana'
- [ ] y 

### 6. What will the following Python code print out?
```
def func(x):
    print(x)

func(10)
func(20)
``` 
- [x] 10
      20
- [ ] x
      20
- [ ] def
      x
      func
      func
- [ ] x
      x

### 7. Which line of the following Python program will never execute?
```
def stuff():
    print('Hello')
    return
    print('World')

stuff()
```
- [ ] return
- [ ] print('Hello')
- [x] print('World')
- [ ] def stuf():
- [ ] stuff()

### 8. What will the following Python program print out?
```
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang = 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'), 'Michael')
```
- [x] Bonjour Michael 
- [ ] def Michael 
- [ ] Hello Michael
- [ ] Hola
      Bonjour
      Hello

### 9. What does the following Python code print out? (Note that this is a bit of a trick question and the code has what many consider to be a flaw/bug - so read carefully).
```
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
```
- [ ] 14
- [x] 2
- [ ] 9
- [ ] 7

### 10. What is the most important benefit of writing your own functions?
- [ ] Following the rule that whenever a program is more than 10 lines you must use a function
- [ ] Following the rule that no function can have more than 10 statements in it
- [x] Avoiding writing the same non-trivial code more than once in your program
- [ ] To avoid having more than 10 lines of sequential code without an indent of de-indent
