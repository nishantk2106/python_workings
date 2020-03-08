def computepay():
    x=int(input("enter hours"))
    y=int(input("enter rate"))
    if x>40:
        z=x-40
        r=(y*1.5)
        gr=(z*r)+((x-z)*y)
    else:
        gr=(x*y)

    print("the gross pay",gr)

computepay()