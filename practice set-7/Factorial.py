# 5! = 5 X 4 X 3 X 2 X 1

num = int(input("enter no. : "))
product = 1
for i in range (1 , num + 1):
    product = product * i

print((f"the factorial of {num} is {product}"))