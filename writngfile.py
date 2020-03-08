fname=input("enter the file name")
fhand=open(fname,'w+')
line1="my name is nishant and i am a student learning python"
line2="dfufdgidhgohurehuihrfhfrivhihiuh uw hfuhu heugh uhfivui uihivhivhih"
fhand.write(line1)
fhand.write(line2)
fhand=open(fname,'r')
for line in fhand:
    line=line.rstrip()
    print(line)
fhand.close()

