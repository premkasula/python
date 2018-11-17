
# Example Program using static variables,methods and
# class methods in instance method

class Employee:
    comp_name = "sathya"
    @staticmethod
    def show():
        print("I am static method")
    @classmethod
    def display(cls):
        print("I am class Method")
        print(cls)
    def info(self):
        print("I am instance method")
        print(self)
        print(self.comp_name) # calling static variable
        self.show() # calling static method
        self.display() # calling class method


e1 = Employee()
e1.info()
print("-------------------")
print(e1.comp_name)
e1.show()
e1.display()



