a=input("enter 4 digit no:")
for x in range(0,len(a)):
    print(a[x],end="")
    print(sum(a[0],a[-1]))
    