# Chapter 9 PY4E Quiz

### 1. How are Python dictionaries different from Python lists?
- [ ] Python lists store multiple values and dictionaries store a single value
- [x] Python lists maintain order and dictionaries do not maintain order
- [ ] Python lists can store strings and dictionaries can only store words
- [ ] Python dictionaries are a collection and lists are not a collection

### 2. What is a term commonly used to describe the Python dictionary feature in other programming languages?
- [ ] Lambdas
- [ ] Sequences
- [ ] Closures
- [x] Associative arrays

### 3. What would the following Python code print out?
```
stuff = dict()
print(stuff['candy'])
```
- [x] The program would fail with a traceback
- [ ] candy
- [ ] -1
- [ ] 0

### 4. What would the following python code print out?
```
stuff = dict()
print(stuff.get('candy',-1))
```
- [ ] 'candy'
- [ ] The program would fail with a traceback
- [x] -1
- [ ] 0

### 5. (T/F) When you add items to a dictionary they remain in the order which you added them? 
- [ ] True
- [x] False

### 6. What is a common use of Python dictionaries in a program?  
- [ ] Computing an average of a set of numbers
- [ ] Splitting a line of input into words using a space as a delimiter
- [ ] Sorting a list of names into alphabetical order
- [x] Building a histogram counting the occurences of various strings in a file

### 7. Which of the following lines of Python is equivalent to the following sequence of statements assuming that *count* is a dictionary?
```
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
```
- [ ] counts[key] = counts.get(key, -1) + 1
- [ ] counts[key] = key + 1
- [ ] counts[key] = (key in counts) + 1
- [x] counts[key] = counts.get(key, 0) + 1
- [ ] counts[key] = (counts[key] * 1) + 1

### 8. In the following Python, what does the *for* loop iterate through?
```
x = dict()
...
for y in x:
    ...
```
- [x] It loops through the keys in the dictionary
- [ ] It loops through alls of the dictionaries in the program
- [ ] It loops through the integers in the range from zero through the length of the dictionary
- [ ] It loops through the values in the dictionary

### 9. Which method in a dictionary object gives you a list of the values in the dictionary?
- [x] values()
- [ ] keys()
- [ ] each()
- [ ] items()
- [ ] all()

### 10. What is the purpose of the second parameter of the *get()* method for Python dictionaries?
- [ ] The key to retrieve
- [x] To provide a default value if the key is not found
- [ ] The value to retrieve
- [ ] An alternate key to use if the first key cannot be found
