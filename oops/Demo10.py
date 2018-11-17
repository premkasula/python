class Employee:
    def assign(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print(self.idno)
        print(self.name)

#  Example of ref object
e1 = Employee()
e1.assign(101,"Ravi")
e1.display()
e1.assign(102,"kumar")
e1.display()
print("----------------------")

# Example of un-ref Object
Employee().assign(1001,"ABCDE")
Employee().display() # Error




