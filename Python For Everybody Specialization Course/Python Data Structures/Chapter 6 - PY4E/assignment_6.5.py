# Write a code using find() and string slicing to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
atnum = text.find('0')
btnum = text.find('5')


answer = text[atnum : btnum+1]
ans = float(answer)
print(ans)
