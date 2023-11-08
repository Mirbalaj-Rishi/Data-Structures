
global totalCost2
totalCost2 = 0 

cost = {"Bananas":1.5,"Apples":2.3,"Oranges":4.5,"Cherries":6}
stock = {"Bananas":35,"Apples":42,"Oranges":40,"Cherries":12}

print("Fruit","Price","stock")
print("----------------------------")

for x in cost:
    print(x,cost[x],stock[x])

def totalCostOfFruit(fruitName,cost,stock):
    global totalCost2
    totalCost = cost * stock
    totalCost2 = totalCost + totalCost2
    return fruitName,totalCost

anotherTotalCost = 0 
print("\n The total value of each fruit")
print("--------------------------------")
for i in cost:
    print(totalCostOfFruit(i,cost[i],stock[i]))
    anotherTotalCost =  totalCost2 + anotherTotalCost

print("\n Here is the total value:",totalCost2)
    
    
