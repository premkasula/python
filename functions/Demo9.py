
def details():
    name = "Ravi"
    cno = 9052492329
    email = "ravi@gmail.com"
    salary = 125000.00
    return name,email,salary,cno

res = details()
print(res)
print(type(res))
print("Salary = ",res[2])