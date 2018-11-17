# Example on static methods
class Employee:
    comp_name = "sathya"  # static variable
    @staticmethod
    def showInfo():  # static method
        print("I am Static Method")
        print(Employee.comp_name)

# calling static method and Variable outside
# the class
Employee.showInfo()
print(Employee.comp_name)