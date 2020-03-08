# Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in
# the list, add it to the list.
x=input("enter the file name :")
a=[]
b=[]
fhand=open(x)
delimiter=" "
for line in fhand:
    line=line.rstrip()
    p=line.split(delimiter)
    a=a+p

[b.append(x) for x in a if x not in b]

c=sorted(b)
print(c)