# Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.
def count(st , letter):
    cnt=0
    for each in st:
        if(each== letter):
            cnt=cnt+1

    return cnt

p=input("enter the character you want to check in string")
j=input("enter the string you want to check")
x=count(j, p)
print(x)