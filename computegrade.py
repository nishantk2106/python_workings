def computegrade():

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