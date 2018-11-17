a=int(input("Enter the a value:"))
b=int(input("enter the b value:"))
negative=bool(input("Enter boolean:"))
def pos_neg(a,b,negative):
    if a>0 or a<0:
        if b>0 or b<0:
            if negative:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(pos_neg(a,b,negative))

