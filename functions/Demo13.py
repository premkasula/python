a = 1000 # Global Variable
def display():
    global a
    a = 99 # Global Variable
    print(a)

print(a)
display()
print(a)
