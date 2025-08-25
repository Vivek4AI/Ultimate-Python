class employee:
    company = "ITC"
    def show(self):
        print(f"the name of the employee is {self.name} an the company is {self.company}.")


# class programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"the name of the employee is {self.name} an the company is {self.company}.")

#     def showlanguage(self):
#         print(f"the name is{self.name} and he is good with{self.language} langugage")

class programmer(employee):
    company = "I T C infotech"
    def showlanguage(self):
        print(f"the name is{self.name} and he is good with{self.language} langugage")

a = employee()
b = programmer()

print(a.company , b.company)

    
