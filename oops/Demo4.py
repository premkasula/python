class Employee:
    @classmethod
    def show(cls):
        print("I am Class Method")
        print(cls)


Employee.show()