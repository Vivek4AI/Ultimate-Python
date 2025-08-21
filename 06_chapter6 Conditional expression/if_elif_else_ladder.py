a = int(input("Enter the age : "))

# if elif else ladder
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you entered an invalid age")

elif(a==0):
    print("You entered 0 which is invalid")
    
else:
    print("you are below the age of consent")

print("End of program")