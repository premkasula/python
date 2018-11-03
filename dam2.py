a = int(input("enter the 1st int value:"))
b = int(input("enter the 2nd int value:"))

def makes10(a,b):
    if a==10 or b==10:
        return True
    elif a+b==10:
        return True
    else:
        return False

print(makes10(a,b))








