def convertTemp(F):
    C = (5.0/9.0)* (F - 32.00)
    return C
print("Fahrenheit, Celsius")
print("-------------------")
for i in range(50, 101, 5):
    Celsius = convertTemp(i)
    print(i,"\t","||" , round(Celsius,2))
