d = {'a':10, 'b':1, 'c':22}
t=list(d.items())
t.sort(reverse=True)
print(t)
for key,val in list(d.items()):
    print(val,key)