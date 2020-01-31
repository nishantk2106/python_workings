from array import *
x= int(input("Enter the length of array "))
arr=array('i',[])
for i in range(x):
    p=int(input("enter the number"))
    arr.append(p)
print("The reverse of array is ")
for i in range(x-1,-1,-1):
    print(arr[i],end=" ")
# arr.reverse()
# print()
# for i in range(x):
#     print(arr[i],end=" ")