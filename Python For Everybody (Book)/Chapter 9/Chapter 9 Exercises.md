# Python For Everybody (Book) (PY4E)

## Chapter 9: Dictionaries Exercises

### Exercise 1. Download a copy of the file www.py4e.com/code3/words.txt
### Write a program that reads the words in *words.txt* and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the *in* operator as a fast way to check whether a string is in the dictionary.
```
word = input('Please enter a string to check whether it is in the file : ')
words = dict()
fname = 'words.txt'
for x in fname:
    if x not in words:
        words[x] = 1
    else:
        words[x] = words[x] + 1

print(word, 'is in the file', words[x], 'times.')

```

### Exercise 2. Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
```
filename = input("Enter a file name: ")
fhand = open(filename, 'r')
days = {}

for line in fhand:
    if line.startswith("From "):
        day = line.split()[2]
        days[day] = days.get(day, 0) + 1

print(days)
```