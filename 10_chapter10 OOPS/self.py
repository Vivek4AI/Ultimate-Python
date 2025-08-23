class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"the language is {self.language}. salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning!")

harry = Employee()
# harry.language = "JavaScript"  # This is an instance attribute
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)