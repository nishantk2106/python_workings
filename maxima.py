numlst=[]
while True:
    x=input("enter the number in the list")
    if (x=='done'):break
    numlst.append(x)

print("Maximum :",max(numlst))
print("Minimum :",min(numlst))