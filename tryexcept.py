# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:


x=input("enter hours")
y=input("enter rate")
try:

    x=int(input("enter hours"))
    y=int(input("enter rate"))
    if x>40:
        z=x-40
        r=(y*1.5)
        gr=(z*r)+((x-z)*y)
    else:
        gr=(x*y)

    print("the gross pay",gr)
except:
    print(" please enter the number ")