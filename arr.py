from array import *
vals=array('i',[5,9,8,4,2])
newvals=array(vals.typecode, (a*a for a in vals))
for g in newvals:
    print(g, end=" ")
print()
for h in range(len(vals)):
    print(vals[h],end=" ")
print()
newvals.reverse()
for g in newvals:
    print(g, end=" ")
print()
newvals.extend()
for g in newvals:
    print(g, end=" ")