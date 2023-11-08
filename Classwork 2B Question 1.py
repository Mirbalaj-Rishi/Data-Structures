
def Factorial_Recursive(n):
    if (n==0):
        # base case
        return 1
    else:
        return n * Factorial_Recursive(n-1)

def Factorial_iterative( n):
    fact = 1
    for i in range( 1, n+1):
        fact = fact * i
    return fact

n = -1

while n < 0:  
    n = int(input("Enter a postive number: "))

f1 = Factorial_iterative(n)
print("The iterative function returned ", f1)


f2 = Factorial_Recursive(n)
print("the recursive function returned ", f2)


