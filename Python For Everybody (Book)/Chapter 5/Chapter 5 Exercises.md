# Python For Everybody (Book) (PY4E)

## Chapter 5: Iteration Exercises

### Exercise 1. Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number detect their mistake using *try* and *except* and print an error message and skip to the next number. 
```
count = 0
total = 0
average = 0

while True:
    str_num = input('Please enter a number: ')
    if str_num == 'done' :
        break
    try:
        flt_num = float(str_num)
    except:
        print('Invalid Input, please enter numeric input')
        continue
    count = count + 1
    total = total + flt_num

average = total / count
print('All done')
print('Total: ', total)
print('Count: ', count')
print('Average: ', average)
```

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid Input
Enter a number: 7
Enter a number: done
16  3  5.3333333333
### Exercise 2. Write another program that prompts for a list of numbers as above and at tht end prints out both the maximum and minimum of the numbers instead of an average.
```
largest = None
smallest = None
while True:
    num = input('Please enter a number:')
    if num == 'done':
        break

    try:
        num = int(num)
    except:
        print('Invalid input, please enter a numeric value:')
        continue

    if largest is None:
        largest = num
    elif largest < num:
        largest = num

    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
        
print('All done')
print('Maximum is', largest)
print('Minimum is', smallest)
```

