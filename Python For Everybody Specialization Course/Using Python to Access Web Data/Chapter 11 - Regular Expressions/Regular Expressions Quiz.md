# Chapter 11 - Regular Expressions - Quiz

### 1. Which of the following best describes "Regular Expressions"?
- [ ] A way to calculate mathematical values paying attention to operator precendence
- [x] A small programming language unto itself
- [ ] The way Python handles and recovers from errors that would otherwise cause a traceback
- [ ] A way to solve Algebra formulas for the unknown value

### 2. What will the '\$' regular expression match? 
- [ ] A dollar sign
- [ ] A new line at the end of a line
- [ ] The beginning of a line
- [x] The end of a line
- [ ] An empty line

### 3. What would the following mean in regular expression [a-z0-9]?  
- [ ] Match any number of lowercase letters followed by any number of digits
- [ ] Match an entire line as long as it is lowercase letters or digits
- [x] Math a lowercase letter or a digit
- [ ] Match any text that is surrounded by square brackets
- [ ] Match anything but a lowercase letter or digit

### 4. What is the type of the return value of the re.findall() method?
- [ ] A string
- [ ] A single character
- [ ] An integer
- [x] A list of strings
- [ ] A boolean

### 5.  What is the "wild card" character in a regular expression (i,e,m the character that matches any character)?
- [ ] *
- [x] .
- [ ] ?
- [ ] ^
- [ ] +
- [ ] $

### 6. What is the difference between the "+" and "*" character in regular expressions? 
- [x] The "+" matches at least one character and the "*" matches zero or more characters
- [ ] The "+" matches upper case characters and the "*" matches lowercase characters
- [ ] The "+" matches the beginning of a line and the "*" matches the end of a line
- [ ] The "+" matches the actual plus character and the "*" matches any character
- [ ] The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"

### 7. What does the "[0-9]+" natch in a regular expression?
- [ ] Any number of digits at the beginning of a line 
- [ ] Zero of more digits
- [x] One or more digits
- [ ] Any mathematical expression
- [ ] Several digits following by a plus sign

### 8. What does the following Python sequence print out?
```
x = 'From: Using the : character'
y = re.findall(^F.+:', x)
print(y)
```
- [ ] From:
- [ ] ^F.+:
- [ ] :
- [ ] ['From:']
- [x] ['From: Using the :']

### 9. What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?
- [ ] $
- [ ] ++
- [ ] ^
- [ ] \g
- [x] ?
- [ ] **

### 10. Given the following line of text:
```
From  stephen.marquard@uct.ac.za  Sat  Jan   5  09:14:16  2008
```
### What would the regular expression '\S+?@\S+' match?
- [ ] From
- [ ] d@uct.ac.za
- [ ] \@\
- [ ] marquard@uct
- [x] stephen.marquard@uct.ac.za
