# Python For Everybody (Book) (PY4E)

## Chapter 8: Lists Exercises

### Exercise 1. Write a function called *chop* that takes a list and modifies it, removing the first and last elements, and returns *None*. Then write a function called *middle* that takes a list and returns a new list that contains all but the first and last elements.
```
def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst)
    new = lst[1:]
    del new[-1]
    return new

test_list = [1, 2, 3, 4]
test_list2 = [1, 2, 3, 4]

chopped_list = chop(test_list)
print(test_list)
print(chopped_list)

middle_list = middle(test_list2)
print(test_list2)
print(middle_list)

```

### Exercise 2. Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it hangles you new text file.
```
fhand = open('test_file.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From ':
        continue
    print(words[2])
```


### Exercise 3. Rewrite the guardian code in the above example without two *if* statements. Instead, use a compound logical expression using the *or* operator with a single *if* statement. 
```
fhand = open('test_file.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
```
### Exercise 4. Find all the unique words in a file.
Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce a list of all the words that Shakespeare used? Would you download all of his work, read it and track all unique words by hand?
Lets use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file *romeo.txt* containing a subset of Shakespeare's work.
To get started download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final results. Write a program to open the file *romeo.txt* and read it line by line. For each line, split the line into a list of words using the *split* function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.
```
lst = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)

```

### Exercise 5. Minimalist Email Client. Write a program to read through the mail box data and when you find line that starts with "From", you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.

This is a good sample output with a few lines removed:
```
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
```
```
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if not line.startswith('From '):
        continue
    email = words[1]
    print(email)
    count += 1
print('There were', count, 'lines in the file with "From" as the first word')
```

### Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done". Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
```
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
```
```
my_list = []                     
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

if my_list:
    print('Maximum: ', max(my_list) or None)
    print('Minimum: ', min(my_list) or None)
```