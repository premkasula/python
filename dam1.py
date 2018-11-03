name=input("enter EMPLOYEE NAME:")
salary=float(input("enter EMPLOYEE SALARY:"))
designation=input("enter EMPLOYEE DESIGNATION:")
manager="m"
analyst="a"
clerk="c"

if designation=="m":
    b=salary*20/100
    salary+=b
    print("Name:",name)
    print("Designation:",designation)
    print("Salary:",salary)
elif designation=="a":
    b=salary*10/100
    salary+=b
    print("Name:",name)
    print("Designation:","a")
    print("Salary:",salary)
elif designation=="c":
    b=salary*5/100
    salary+=b
    print("Name:",name)
    print("Designation:",designation)
    print("Salary:",salary)
else:
    print("input type should be m/a/c")

