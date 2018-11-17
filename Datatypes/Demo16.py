
def first_last6(a):
    if a[0]==6 or a[-1]==6:
        return True
    else:
        return False

res = first_last6([13,6,1,2,3])
print(res)