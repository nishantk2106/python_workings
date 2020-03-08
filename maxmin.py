
a=[]
max=0
min=999999
for i in range(1000000):
    x=input("enter the number")
    a.append(x)

    try:
        p=int(a[i])
        if(p>max):
            max=p
        if min>p:
            min=p
    except:
        if(a[i]=='done'):
            print(max,min)
            break
        else:
            print("invalid input")




