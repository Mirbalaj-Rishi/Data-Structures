num = -1 

while True:
    num = int(input("Please input an positive number: "))
    if num >= 0:
        break
print(num)
for i in range(0,num+1):
    print(i)
