a=0
b=1
c=0
print(a)
print(b)
for j in range(2,100,1):
    sum=a+b
    print(sum)
    a=b
    b=sum
    c=c+1
    if(c<=50):
        continue
    else:
        break
print("Bye")
