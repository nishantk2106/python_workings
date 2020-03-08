#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range, print an error message. If the score is between 0.0 and 1.0,
#print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6
y=input("enter score ")
try:
    x=float(y)
    if x>=0.9 and x<1.0:
        print("A")
    elif x>=0.8 and x<1.0:
        print("B")
    elif x>=0.7 and x<1.0:
        print("C")
    elif x>=0.6 and x<1.0:
        print("D")
    elif x<=0.6:
        print("F")
    else:
        print("bad score")
except:
    print("bad score ")