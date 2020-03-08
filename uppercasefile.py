x=input("enter the file name")
fhand=open(x)
for line in fhand:
    line=line.rstrip()
    print((line.upper()))
