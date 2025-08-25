try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    print(f"the division a/b is {a/b}")

except ZeroDivisionError as v:
    print("Infinite")