def details(idno=0,name=None,salary=0.0):
    print("Employee Details")
    print("IDNO : ",idno)
    print("NAME : ",name)
    print("SALARY : ",salary)

details()
details(101)
details(102,"kumar")
details(salary=125000.00)