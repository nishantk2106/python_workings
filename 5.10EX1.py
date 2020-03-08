
a=[]
c=0
total=0
for i in range(1000000):
    x=input("enter the number")
    a.append(x)
    try:
        p=int(a[i])
        if(p>0):
            c=c+1
            total=total+int(a[i])

    except:
        if(a[i]=='done'):
            print(total,c,(total/c))
            break
        else:
            print("invalid input")




