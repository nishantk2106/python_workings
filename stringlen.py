# Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.

x=input("enter the string")
index=len(x)-1
while index>=0:
    # print(x[index],end=" ")
    index=index-1
print(x.encode(encoding="utf-8", errors="strict"))