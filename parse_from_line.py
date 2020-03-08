x=input("Enter the file name :")
a=0
b=[]
delimit=" "
try:
    fhand=open(x,'r')
except:
    print("file does not exist ")
    exit()
for line in fhand:
    line.rstrip()
    if line.startswith('From '):
        line.rstrip()
        line=line.split(delimit)
        a=a+1
        print(line[1])

print("There were",a,"lines in the file with From as the first word")