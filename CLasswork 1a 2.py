def factorial(n):
    product=1
    for i in range(1,n+1):
        product = product * i
        return product
num = -1
while num<0:
    num = int( input( " Enter a positiveinteger: "))
f = factorial(num)
print(" The Factorial is ", f)
