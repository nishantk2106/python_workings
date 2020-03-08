# Exercise 2: Write a program to prompt for a file name, and then read through the
# file and look for lines of the form:
#     X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.


x=input("enter the file name ")
fhand=open(x)
sum=0
count=0
for line in fhand:
    if (line.startswith('X-DSPAM-Confidence:')):
        p=line.find(':')
        line=line[p+1:]
        fl=float(line)
        sum=sum+fl
        count=count+1

print("Average spam confidence ",sum/count)