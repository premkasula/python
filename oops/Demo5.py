class Employee:
    @classmethod
    def display(cls):
        print("I am class method")
        print(cls.comp_name) # calling static variable
        cls.show() # calling static method

    @staticmethod
    def show():
        print("I am static method")

    comp_name = "sathya"  # static variable

Employee.display() # calling class method
