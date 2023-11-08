import math 

def getArea(radius):
    A = radius * math.pi * radius
    return A


def getCircumference(radius):
    C = 2 * math.pi * radius
    return C

print("Radius,\t||,Cicumference,||, Area")
for i in range(1, 11):
    
    print(i,"\t","||" ,round(getCircumference(i)),"\t","      ","||", round(getArea(i)))
