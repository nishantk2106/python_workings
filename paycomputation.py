# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.

x=int(input("enter hours"))
y=int(input("enter rate"))
if x>40:
    z=x-40
    r=(y*1.5)
    gr=(z*r)+((x-z)*y)
else:
    gr=(x*y)

print("the gross pay",gr)
