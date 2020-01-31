namelst = []
n = int(input("enter the size of the list"))
for i in range(n):
    x = input("Enter the name")
    namelst.append(x)

def count(namelst):
    c=0
    for i in range(n):
        x=len(namelst[i])
        if(x>=5):
            c=c+1

    print(c)

count(namelst)