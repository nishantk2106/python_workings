fname=open("romeo.txt",'r')
lst=list()
lst1=list()
c=list()
d=dict()
tp=tuple()
for i in fname:
    i=i.rstrip()
    i=i.lower()
    i=i.split()
    for p in i:
     lst.append(p)
for t in lst:
    c=list(t)
    for a in c:
        if a not in d:d[a]=1
        else:d[a]+=1
for key,val in list(d.items()):
    lst1.append((val,key))
lst1.sort(reverse=True)
for key,value in lst1:
    print(value,key)





