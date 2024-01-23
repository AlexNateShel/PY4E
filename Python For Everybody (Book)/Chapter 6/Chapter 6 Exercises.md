# Python For Everybody (Book) (PY4E)

## Chapter 6: Strings Exercises

### Exercise 1. Write a *while* loop that starts at the last character in the string and wroks its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
```
word = input('Please enter a string: ')
index = len(word) - 1
while index >= 0:
    letter = word[index]
    print(letter)
    index -= 1
```

### Exercise 2. Given that fruit is a string what does fruit[:] mean?
- All of the characters in fruit.

### Exercise 3. Encapsulate this code in a function named __count__, and generalize ir so that it accpets the string and the letter arguments.
The following program counts the number of times the letter "a" 
appears in a string.
```
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
```
EXERCISE: Encapsulte this code in a function named count, and
generalize it so that it accepts the string and the letter as arguments
```
def count(string, letter):
    counter = 0
    for char in string:
        if char == letter:
        counter += 1
    
    return counter

print(count('banana', 'a'))
```

### Exercise 4. Write an invocation that counts the number of times the letter a occurs in "banana".
```
str = 'banana'
print(str.count('a'))
```

### Exercise 5.  Write a code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
```
text = "X-DSPAM-Confidence:    0.8475"
atnum = text.find('0')
btnum = text.find('5')


answer = text[atnum : btnum+1]
ans = float(answer)
print(ans)
```