class employee:
    def __init__(self):
        print("construstor of employee")
    a = 1

class programmer(employee):
    def __init__(self):
        print("construstor of programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("construstor of manager")
    c = 3


# o = employee()
# print(o.a) # print 'a' attribute
# # print(o.b) # Shows an error as there is no b attribute in employee class.

# o = programmer()
# print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)