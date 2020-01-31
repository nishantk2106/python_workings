def count(lst):
        even=0
        odd=0
        for i in lst:
            if i%2 ==0:
                even=even+1
            else:
                odd=odd+1
        return odd,even

numlst=[]
n=int(input("enter the size of the list"))
for i in range(n):
    x=int(input("Enter the value"))
    numlst.append(x)


odd,even=count(numlst)
print(even)
print(odd)