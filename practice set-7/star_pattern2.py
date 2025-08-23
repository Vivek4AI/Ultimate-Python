
num = int(input("enter no. : "))

for i in range (1 , num+1):
    print(" "* (num-i),)
    print("*"* i , end = "")
    print("")