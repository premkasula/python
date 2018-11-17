
class Employee:
    comp_name = "sathya"
    def display(self):
        idno = 101
        print("Display Method")
        print(Employee.comp_name)

e1 = Employee()
# calling Method using ref variable
e1.display()