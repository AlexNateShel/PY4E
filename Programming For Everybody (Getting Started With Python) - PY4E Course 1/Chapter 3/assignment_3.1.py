# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 

hrs = input('Please enter your hours')
rate = input('Please enter your hourly rate')
h = float(hrs)
r = float(rate)
if h <= 40:
    pay = h * r
else:
    ovtime_hrs = h - 40
    ovtime_rate = r * 0.5
    pay = (h *r) + (ovtime_hrs * ovtime_rate)
print(pay)

