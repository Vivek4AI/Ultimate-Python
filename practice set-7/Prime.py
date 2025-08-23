num = int(input("enter no. : "))

for i in range (1 , num+1):
    print(" "* (num-i),end = "")
    print("*"* (2 * i -1), end = "")
    print("")
for i in range (2, num):
    if(num%i == 0):
        print("Not prime")
        break
else:
    print("Prime")

   
   


