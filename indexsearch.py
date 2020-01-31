from array import *
x= int(input("Enter the length of array"))
arr=array('i',[])
for i in range(x):
    p=int(input("enter the number"))
    arr.append(p)
d=int(input("Enter the number you want to search index of "))
k=0
for i in range(x):
    if(arr[i]==d):
        print("the index of", d, "is", k)
        break
    else:
        k=k+1

# print(arr.index(d))