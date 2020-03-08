fname=input("Enter the file name ")
try:
    fhand=open(fname)
    count=0
    for line in fhand:
        line=line.rstrip()
        if line.startswith('From:'):
            count=count+1
            print(line)
    print("total number of mail received:", count)

except:
    print("cannot open the file",fname)
    exit()

