class Employee:
    def __init__(self):
        print("Object Created")

    def show(self):
        print("I am show")

    def __del__(self):
        print("Object Deleted")

Employee().show()
Employee().show()
