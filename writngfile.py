fname=input("enter the file name")
try:
    fhand=open(fname,)
except:
    print("cannot open the file name",fhand)
    exit()

line1="my name is nishant and i am a student learning python"

fhand.write(line1)
line2="dfufdgidhgohurehuihrfhfrivhihiuh uw hfuhu heugh uhfivui uihivhivhih"
fhand.write(line2)
fhand.close()

