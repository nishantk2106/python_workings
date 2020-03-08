print("python egg.py")
f=input("Enter the file name :")
try:
    fhand=open(f)
    count=0
    for line in fhand:
        if (line.startswith("Subject")):
            count=count+1
    print("There were ",count,"subject lines in ",f)
except:
    if f=="na na boo boo":
        print(f ,"to you - You have been punk'd!")
    else:
        print("file cannot be opend :",f)




