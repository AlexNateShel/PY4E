# Python For Everybody (Book) (PY4E)

## Chapter 3: Conditional Execution Exercises

### Exercise 1. Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
```
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

hours = input('Please enter your hours:')
rate = input('Please enter your hourly rate:')
if hours > 40:
    pay = 40 * rate + (hours - 40) * (rate * 1.5)
else:
    pay = hours * rate

print('Pay: ', pay)
```

### Exercise 2. Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two execptions of the program:
```
Enter Hours: 20
Enter Rate: nine
Error, please enter a numeric input

Enter Hours: forty
Error, please enter a numeric input

input_hours = input('Please enter your hours:')
try:
    hours = float(input_hours)
except ValueError:
    print('Error, please enter numeric input')
    quit()

input_rate = input('Please enter your hourly rate:')
try: 
    rate = float(input_rate)
except ValueError:
    print('Error, please enter numeric input')
    quit()

if hours > 40:
    pay = 40 * rate + (hours - 40) * (rate * 1.5)
else:
    pay = hours * rate

print('Pay: ', pay)
```

### Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
 Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
```
score = 0.0                               
grade = ""

input1 = input('Enter score: ')
try:
    score = float(input1)                
except ValueError:
    print('Bad score')
    quit()

if 0.0 <= score <= 1.0:                 
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'Bad score'

print(grade)
```
