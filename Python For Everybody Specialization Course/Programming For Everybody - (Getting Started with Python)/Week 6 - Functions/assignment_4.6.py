# PY4E - Python For Everybody Assignment 4.6 
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number. 

def computepay(h, r) :
    computed = h * r
    return computed

hrs = input('Enter hours:')
h = float(hrs)
rate = input('Enter rate:')
r = float(rate)
if h <= 40 :
    p = computepay(h * r)
    print('Pay', p)
else :
    oth = h - 40
    othr = r * 0.5
    pay1 = (h * r) + (oth * othr)
print('Pay', pay1)