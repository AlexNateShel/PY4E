# Chapter 5 (PY4E) Quiz

### 1. What is wrong with this Python loop:
```
n = 5
while n > 0 :
    print(n)
print('All done')
```
- [x] This loop will run forever 
- [ ] The __print('All done')__ statement should be indented four spaces
- [ ] There should be no colon on the __while__ statement
- [ ] __while__ is not a Python reserved word

### 2. What does the __break__ statement do?  
- [ ] Jumps to the "top" of the loops and starts the next iteration
- [x] Exits the currently executing loop
- [ ] Resets the iteration variable to its intial value 
- [ ] Exits the program

### 3. What does the __continue__ statement do?   
- [ ] Exits the currently executing loop
- [ ] Resets the iteration variable to its intial value 
- [ ] Exits the program
- [x] Jumps to the "top" of the loops and starts the next iteration

### 4. What does the following Python program print out?
```
tot = 0 
for i in [5, 4, 3, 2, 1]
    tot = tot + 1
print(tot)
```   
- [x] 5
- [ ] 0
- [ ] 15
- [ ] 10

### 5. What is the iteration variable in the following Python code:
```
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```  
- [x] friend
- [ ] Sally
- [ ] Glenn
- [ ] Joseph

### 6. What is a good description of the following bit of Python code?
```
zork = 0
for thing in [9, 41, 12, 3, 74, 15]
    zork = zork + thing
print('After', zork)
```  
- [x] Sum all the elements of a list
- [ ] Count all of the elements in list
- [ ] Find the smallest item in a list
- [ ] Compute the average of the elements in a list

### 7. What will the following code print out?
```
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15]
    if the_num < smallest_so_far :
        smallest_so_far = the_num
print(smallest_so_far)
```
### Hint: This is a trick question and most would say this code has a bug - so read carefully
- [x] -1
- [ ] 74
- [ ] 42
- [ ] 3

### 8. What is a good statement to describe the __is__ operator as used in the following statement:
```
if smallest is None:
    smallest = value
``` 
- [ ] The if statement is a syntax error 
- [ ] Looks up 'None' in the **smallest** variable if it is a string
- [ ] Is true if the **smallest** variable has a value of -1
- [ ] Matches both type and value

### 9. Which reserved word indicates the start of an "indefinite" loop in Python?
- [x] while
- [ ] indef
- [ ] def
- [ ] for 
- [ ] break

### 10. How many times will the body of the following loop be executed?
```
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')
```  
- [ ] This is an infinite loop
- [x] 0
- [ ] 1
- [ ] 5
