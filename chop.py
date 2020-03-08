from math import floor
numlst=[]
def chop1(n):
    s=len(numlst)
    print(numlst[0],numlst[s-1])
def middle(numlst):
    s=len(numlst)
    p=floor(s/2)
    print(numlst[p])
# driver code
if __name__=="__main__":
    while True:
        x=input("enter the value :")
        if(x =='done'):
            break
        numlst.append(x)
    chop1(numlst)
    middle(numlst)