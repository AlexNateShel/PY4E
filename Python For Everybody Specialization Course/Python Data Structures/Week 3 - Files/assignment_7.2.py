# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:   0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce and output as shown below.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# When you are testing below enter 'mbox-short.txt' as the file name.

# Desired Output
# Average spam confidence: 0.7507185185185187

count = 0
total = 0
fname = input('Please enter a file name: ')
fh = open(fname)
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count += 1
        a = line.find('0')
        x = line[a:]
        total = total + float(x)
        
average = total / count
print('Average spam confidence: ', average)