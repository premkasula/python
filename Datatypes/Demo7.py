
t1 = 10,20,30 # packing
print(t1)
print(type(t1))

a,b,c = t1 # un packing
print(a,type(a))
print(b,type(b))
print(c,type(c))


t2 = 10,10.25,"sathya",False # packing
print(t2)
print(type(t2))

no,avg,name,status = t2 # un packing
print(no,type(no))
print(avg,type(avg))
print(name,type(name))
print(status,type(status))

print("--------------------------------")

# We cant put one object(item) with in the ()
t3 = (10)
print(t3)  # 10
print(type(t3))  # <class 'int'>


t3 = (10,)
print(t3)  # (10)
print(type(t3))  # <class 'tuple'>








