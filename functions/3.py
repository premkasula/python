def fun1():
    print("fun 1")
def fun2():
    print("fun 2")
    def fun1():
        print("fun 1")
    fun1()
fun1()
fun2()
