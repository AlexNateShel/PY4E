# Write a program to prompt the user for hours and rate per hour using the input to copute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program. (The pay should be 96.25)
# You should use input to read a string and float() to convert the string into a number.

hrs = input('Please enter your hours')
rate = input('Please enter your hourly rate')
pay = float(rate) * float(hrs) 
print('Pay:', pay)
