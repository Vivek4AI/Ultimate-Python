class Employee :
    language = "python" # class attribute
    salary = "1200000"  # class attribute

harry = Employee()
harry.name ="harry" # instance attribute
print(harry.name,harry.language,harry.salary)

rohan = Employee()
rohan.name = "rohan robinson roro"
print(rohan.salary,rohan.name,rohan.language)

# Here name is an instance attribute and salary and language is class attribute.