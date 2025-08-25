a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if(b == 0):
    raise ZeroDivisionError("hey , what are u doing?? huhhh, our program is not meant to divide by zero.")
else:
    print(f"the division a/b is {a/b}")