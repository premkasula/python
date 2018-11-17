d_value = "Not Assigned"
class Employee:
    def __init__(self,idno=d_value,name=d_value,salary=d_value):
        self.idno = idno
        self.name = name
        self.salary = salary
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)
        print("SALARY = ",self.salary)

e1 = Employee()
e1.display()
print("-----------------")
e2 = Employee(salary=125000.00)
e2.display()

