#these global variables are used in all functions 

global hall
global mez

#starting amounts of seats
mez = 100
hall = 300


#this function tells the user how many seats are left
def whatsLeft():
    global hall
    global mez
    print(f"There are now {hall} Hall seats left, and {mez} Mezzanine seats")
    
#this checks to make sure that there are enouph seats left and then subtracts the amount of seats based on previous inputs
def hallFunction():
    global hall
    #this asks the user for the number of adults and number of children and stores that value
    print("A Hall seat is $10 per adult and $7 per child")
    adults = int(input("Please type the number of adults: "))
    children = int(input("Please type the number of children: "))
    # this adds up the amount of tickets and makes sure that there are enouph empty seats left
    # if there aren't enouph seats left it will tell the user the sale is not possible beucase there are only 
    newHallTotal = adults + children
    if hall - newHallTotal < 0:
        print(f"sorry I can't do that, you asked for {newHallTotal} seats when there are only {hall} seats left.")
    else:
        # calulates the cost of the seats
        adultCost = adults * 10 
        childCost = children * 7 
        total = childCost + adultCost
        print(f"Ok that will be ${adultCost} for {adults} adults, and ${childCost} for {children} children, that all comes up to a total of ${total}")
        # this part subtracts to find out the amount of seats that are left and updates the variable
        hall = hall - newHallTotal 

#this checks to make sure that there are enouph seats left and then subtracts the amount of seats based on previous inputs
def mezFunction():
    global mez
    #this asks the user for the number of adults and number of children and stores that value
    print("A Mezzanine seat is $8 per adult and $5 per child")
    adults = int(input("Please type the number of adults: "))
    children = int(input("Please type the number of children: "))
    # this adds up the amount of tickets and makes sure that there are enouph empty seats left
    # if there aren't enouph seats left it will tell the user the sale is not possible beucase there are only 
    newMezTotal = adults + children
    if mez - newMezTotal < 0:
        print(f"sorry I can't do that, you asked for {newMezTotal} seats when there are only {mez} seats left.")
    else:
        # calulates the cost of the seats
        adultCost = adults * 8
        childCost = children * 5
        total = childCost + adultCost
        print(f"Ok that will be ${adultCost} for {adults} adults, and ${childCost} for {children} children, that all comes up to a total of ${total}")
        # this part subtracts to find out the amount of seats that are left and updates the variable
        mez = mez - newMezTotal
        


#this allows the function to loop as long as there are seats avaliable 
while not hall <= 0 or not mez <= 0:
    #this function lets the viewer know how many seats are left
    whatsLeft()
    #this input determines whether the program calulates one type of input or the other
    userImput = input("press 1 for Hall seats or press 2 for Mezzanine seats: ")
    
    if userImput == "1":
        # lets the user know what they selected
        print("you have selected Hall seats")    
        hallFunction()
    elif userImput == "2":
         # lets the user know what they selected
        print("you have selected Mezzanine seats")
        mezFunction()
    else:
        print("invalid input")
print("There are no more seats avaliable....sorry")


