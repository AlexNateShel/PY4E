# Python For Everybody (Book) (PY4E)

## Chapter 4: Functions Exercises

### Exercise 4. What is the purpose of the "def" keyword in Python?
- [ ] It is slang that means "the following code is really cool"
- [ ] It indicates the start of a function
- [ ] It indicates that the following indented section of code is to be stored for later
- [ ] b and c are both true
- [ ] None of the above

### Exercise 5. What will the following Python program print out?
```
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()
```
- [ ] Zap ABC jane fred jane
- [ ] Zap ABC Zap
- [ ] ABC Zap jane
- [x] ABC Zap ABC
- [ ] Zap Zap Zap

### Exercise 6. Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters (hours and rate).
```
Enter Hours: 45
Enter Rate: 10
Pay 475.0

def computepay(tmp_hours, tmp_rate):
    if tmp_hours <= 40:
        return tmp_hours * tmp_rate
    
    overtime = tmp_hours - 40 
    return (tmp_hours * 40) + (1.5 * tmp_rate * overtime)

def check_for_float(inputx):
    try:
        val = float(inputx)
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()


input_hours = input('Please enter your hours:')
hours = check_for_float(input_hours)

input_rate = input('Please enter your rate:')
rate = check_for_float(input_rate)

pay = computepay(hours, rate):
print('Pay: ', pay)
```

### Exercise 7. Rewrite the grade program from the previous chapter using a function called computegrade that takes score as its parameter and returns a grade as a string.
```
def computegrade(tmp_score):
    if 0.0 <= tmp_score <= 1.0:
        if tmp_score >= 0.9:
            return 'A'
        if tmp_score >= 0.8:
            return 'B'
        if tmp_score >= 0.7:
            return 'C'
        if tmp_score >= 0.6:
            return 'D'
        return 'F'
    return 'Bad score'

input_score = input('Please enter your score:')
score = 0.0

try:
    score = float(input_score)
except ValueError:
    print('Bad score')
    quit()

grade = computegrade(score)
print(grade)
```