d=dict()
lst=list()
try:
    fhand=open("mbox-short.txt",'r')
except:
    print("cannot find the file in directory ")
    exit()
for lines in fhand:
    lines=lines.rstrip()
    if lines.startswith('From '):
        lines=lines.split()
        lines=lines[5]
        lines=lines.split(":")
        lines=lines[0]
        if lines not in d:d[lines]=1
        else:d[lines]+=1
for key,val in list(d.items()):
    lst.append((key,val))
lst.sort()
for k,v in lst:
    print(k,v)