
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words)==0:continue
    if words[0] != 'From' : continue
    print(words[2])
