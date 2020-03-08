x=input("Enter the file name :")
a=[]
try:
    handle=open(x,'r')
except:
    print("File does not exist")
    exit()
for line in handle:
    line=line.rstrip()
    line=line.split()
    a=a+line
print(sorted(a))

# romeo.txt
