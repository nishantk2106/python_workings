data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
lpos=data.find(' ',atpos)
print(lpos)
newdat=data[atpos+1:lpos]
print(newdat)
print('I have spollted a camel at %s'% newdat)