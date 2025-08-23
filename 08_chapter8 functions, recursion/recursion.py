'''
facotrial(1) =  1 
facotrial(2) =  2 x 1 
facotrial(3) =  3 x 2 x 1 
facotrial(4) =  4 x 3 x 2 x 1 
facotrial(5) =  5 x 4 x 3 x 2 x 1 
facotrial(n) = n x (n-1) x.......... 3 x 2 x 1 

factorial(n) = n * factorial(n-1)

'''

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)
      
n = int(input("Enter a number : "))
print(f"the factorial of this no.{factorial(n)}")