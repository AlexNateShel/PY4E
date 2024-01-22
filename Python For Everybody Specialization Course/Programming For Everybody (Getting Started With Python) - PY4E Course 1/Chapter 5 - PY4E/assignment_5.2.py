# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the number
# If the user enters anything other than a valid number catch it with a try/except and put out and appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4, to test the the output.

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

print('Maximum is', largest)
print('Minimum is', smallest)
