#  Chapter 6 (PY4E) Quiz 

### 1. What does the following Python program print out?
```
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
```
- [x] Hellothere
- [ ] Hello
- [ ] Hello there
- [ ] Hello
      there

### 2. What does the following Python program print out?
```
x = '40'
y = int(x) + 2
print(y)
```
- [x] 42
- [ ] x2
- [ ] 402
- [ ] int402

### 3. How would you use the index operator [] to print out the letter q from the following string?
```
x = 'From marquard@uct.ac.za'
```   
- [ ] print(x[7])
- [x] print(x[8])
- [ ] print(x[q])
- [ ] print(x[9])
- [ ] print(x[-1])

### 4. How would you use string slicing [:] to print out 'uct' from the following string?
```
x = 'From marquard@uct.ac.za'
```
- [ ] print(x[15:18])
- [ ] print(x[15:3])
- [ ] print(x[14+17])
- [ ] print(x[14:3])
- [x] print(x[14:17])
- [ ] print(x[14/17])

### 5. What is the iteration variable for the following Python code?
```
for letter in 'banana' :
    print(letter)
```
- [ ] 'banana'
- [ ] for
- [ ] in
- [ ] print
- [x] letter

### 6. What does the following Python code print out?
```
print(len('banana')*7)
```  
- [ ] banana7
- [x] 42
- [ ] 0
- [ ] bananabananabananabananabananabananabanana

### 7. How would you print out the following variable in all upper case in Python?
```
greet = 'Hello Bob'
```
- [ ] puts(greet.ucase)
- [ ] print(uc($greet));
- [ ] print(greet.toUpperCase());
- [ ] print(greet.upper())

### 8. Which of the following in __not__ a valid string method in Python?
- [x] boldface()
- [ ] upper()
- [ ] lower()
- [ ] lstrip()
- [ ] startswith()

### 9. What will the following Python code print out?
```
data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
``` 
- [ ] mar
- [ ] uct
- [ ] Sat
- [x] .ma

### 10. Which of the following string methods removes whitespace from both the beginning and end of a string? 
- [ ] strtrunc()
- [ ] split()
- [ ] wsrem()
- [x] strip()
