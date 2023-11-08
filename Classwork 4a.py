import random
list = []
for i in range(0,10):
    userInput = int(input("Enter an integer: "))
    list.append(userInput)
print(list)
print("Here is the sum,", sum(list))
print("Here is the min,", min(list))
print("Here is the max,", max(list))
print("Here is the length,", len(list))


print("Here is the unshuffled list,",list)
random.shuffle(list)

print("Here is the shuffled list,",list)
list.sort()
print("Here is the sorted list,",list)
noDuplicates = []
for x in list:
    if x not in noDuplicates:
        noDuplicates.append(x)
print("Here is the list without any duplicates,",noDuplicates)
