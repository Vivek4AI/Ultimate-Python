def greatest(a , b , c):
    if( a > b and a > c):
        print("a is greatest ", a)
    elif( b > a and b > c):
        print("b is greatest ", b)
    else:
        print("c is greatest ", c )

a = int(input("enter num 1 : "))
b = int(input("enter num 2 : "))
c = int(input("enter num 3 : "))
print(greatest(a,b,c))