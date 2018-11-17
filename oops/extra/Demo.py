
from OOPS.Extra.sample1 import Address

class Employee:
    def assign(self,id,na,dno,area):
        self.idno = id
        self.name = na
        self.add = Address()
        self.add.assign(dno,area)

    def display(self):
        print(self.idno)
        print(self.name)
        self.add.display()

idno = int(input("Enter IDNO : "))
name = input("Enter Name : ")
dno = int(input("Enter Door No : "))
area = input("Enter Area : ")

emp1 = Employee()
emp1.assign(idno,name,dno,area)
emp1.display()










