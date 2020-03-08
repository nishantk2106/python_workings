# Exercise 5: Write a program to read through the mail box data and when you
# find line that starts with “From”, you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on
# the From line.

x=input("Enter the file name")
fhand=open(x)
for line in fhand:
    line=line.rstrip()
    if not  (line.startswith("From:")):continue
    p=line.split()
    print(p[1])