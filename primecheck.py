x=int(input("Enter the number you want to check:"))
c=0
for i in range(1,x+1,1):
    if (x%i==0):
         c=c+1
    else:
        continue

if(c==2):
        print(x,"is a prime number")
else:
    print(x,"is not a prime number")