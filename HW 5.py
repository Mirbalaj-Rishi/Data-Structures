class Node:
     def __init__(self, name, price, stock):
         self.name = name
         self.price = price
         self.stock = stock
         self.ref = None

class LinkedList:
     # ---------------Create an empty linked list -------------
     
     def __init__(self):
         self.start_node = None

    #  ------------- Insert at start  ----------------------         
     def insert_at_start(self, name, price, stock):
            new_node = Node(name, price, stock)
            new_node.ref = self.start_node
            self.start_node = new_node
            
    # --------------- Traverse the linked list  ----------------------
     
     def traverse_list(self):
         print("Here is the Product List")
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 print(f"Name: {n.name} | Price: {n.price} | stock: {n.stock}")
                 n = n.ref
         print(" ")

   # --------------- Print lowstock items  ----------------------
     
     def lowStock(self):
         print("Here are the items with less than 20 pounds left")
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 if n.stock < 20: 
                      print(f"Name: {n.name} | Price: {n.price} | stock: {n.stock}")
                 n = n.ref
         print(" ")
        # --------------- print out prices above a certin price  ----------------------
     
     def findPriceOfStuff(self,x):
         print(f"Here is everything above ${x}")
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 if n.price > x:
                     print(f"Name: {n.name} | Price: {n.price} | stock: {n.stock}")
                 n = n.ref
         print(" ")





# ___________ USER COMMANDS ______________________

"""
My test inputs

avacado 30 40
orange 40 20 
banna 10 30
"""


productList = LinkedList()


loop = "yes"

while loop == "yes":
    print("""Type 'insert info' to add information to the linked list
Type 'print info' to print all information in the linked list
Type 'find prices' to print items above a certian price
Type 'print stock' to print items that have less than 20 pounds of stock left""")
    choice = input()
    choice = choice.lower()
    if choice == "insert info":
        loop = "no"
        ok = "no"
        while ok == "no":
            try:
                name, price, stock = input("Please give the name the price and the stock in that order on a single line with spaces seperating them: ").split()
                price = float(price)
                stock = float(stock)
                ok = "yes"
            except:
                print("Invalid input returning to previous section, please don't put any '$' or other additional symbols into price or stock")
                ok = "no"
            productList.insert_at_start(name, price, stock)
        ok = "no"
        loop = "yes"
        print(f"Name: {name} | Price: {price} | Stock: {stock} | Inserted into the list")
    elif choice == "print info":
        productList.traverse_list()
    elif choice == "find prices":
        ok2 = "no"
        while ok2 == "no":
            try:
                pricesInput = input("Please give the lowest price: ")
                pricesInput = float(pricesInput)
                print(pricesInput)
                productList.findPriceOfStuff(pricesInput)
                ok2 = "yes"
            except:
                print("Invalid input, please only put a number with no symbols")
                ok2 = "no"
    elif choice == "print stock":
        productList.lowStock()
    else:
        print("Invalid input returning to main menu")
        loop = "yes"

    
            
    





