def div (a,b):
    print("the division of the teo values are ", a/b)

def smart_div(func):

    def inner(x,y):
        if(x<y):
            x,y=y,x
        return func(x,y)
    return inner
div=smart_div(div)
x=int(input("enter the first value"))
y=int(input("enter the second value"))

div(x,y)
