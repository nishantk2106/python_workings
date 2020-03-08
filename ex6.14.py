str = 'X-DSPAM-Confidence:0.8475'
atpos=str.find(':')
print(atpos)
str1=str[atpos+1:]

print((float(str1)))
