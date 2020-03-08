# write a small program that looks for lines where the line starts with “From”, split
# those lines, and then print out the third word in the line:
x=input("Enter the file name :")
try:
    fhand =open(x)
    for line in fhand:
        line=line.rstrip()
        if not line.startswith('From '): continue
        x=line.split()
        print(x)

except:
    print("cannot open the file",fhand)
    exit()