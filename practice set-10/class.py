class programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p1 = programmer("harry","1200000",110081)
print(p1.name , p1.company , p1.salary , p1.pincode) 

p2 = programmer("shivansh", "150000", 245001)
print(p2.company , p2.salary , p2.name , p2.pincode)
