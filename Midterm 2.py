class Node:
    def __init__(self, teamName, problems, time):
         self.teamName = teamName
         self.problems = problems
         self.time = time
         self.ref = None

class LinkedList:
     # ---------------Create an empty linked list -------------
     
    def __init__(self):
         self.start_node = None

    #  ------------- Insert at start  ----------------------         
    def insert_at_start(self, teamName, problems, time):
            new_node = Node(teamName, problems, time)
            new_node.ref = self.start_node
            self.start_node = new_node
            
    # --------------- Traverse the linked list  ----------------------
     
    def traverse_list(self):
         print("Here is the Team List")
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 print(f"Team Name: {n.teamName} | Problems Solved: {n.problems} | Time Taken: {n.time}")
                 n = n.ref
         print(" ")

   # --------------- Print lowstock items  ----------------------

newList = LinkedList()
class LinkedList:
    def lowStock(self):
         print("Here are the teams that solved more than 3 problems")
         if self.start_node is None:
             print("List is empty - there are no teams")
             return
         else:
             n = self.start_node
             while n is not None:
                 if n.problems > 3: 
                      print(f"Team Name: {n.teamName} | Problems Solved: {n.problems} | Time Taken: {n.time}")
                 n = n.ref
         print(" ")


        # --------------- print out prices above a certin price  ----------------------

    def findTime(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        max = n.time
        while n is not None:
            if n.time > max:
                max = n.problems
            n = n.ref
        return max
    
    def findteamfortime(self, x):
        print(f"Here is/are the Winner(s)")
        if self.start_node is None:
             print("List is empty")
             return
        else:
             n = self.start_node
             while n is not None:
                 if n.problems == x:
                     print(f"Team Name: {n.teamName} | Problems Solved: {n.problems} | Time Taken: {n.time}")
                 n = n.ref
        print(" ")
     
    def findPriceOfStuff(self, x):
         print(f"Here is/are the Winner(s)") 
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 if n.problems == x:
                     newList.insert_at_start(n.teamName, n.problems, n.time)
                 n = n.ref
         print(newList.findteamfortime(newList.findTime()))





        #__________________ Get Max

    def getMax(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        max = n.problems
        while n is not None:
            if n.problems > max:
                max = n.problems
            n = n.ref
        return max

    #___________ Average
    def getAverage(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        sum = 0 
        while n is not None:
            sum = sum + n.time
            count = count + 1
            n = n.ref
        average = sum / count
        return average

# ___________ USER COMMANDS ______________________


productList = LinkedList()


loop = "yes"

while loop == "yes":
    print("""Type 'Insert Team' to add information to the linked list
Type 'print info' to print all information in the linked list
Type 'Average Time' to print out the average time taken
Type 'Three Problems' to print out teams that solved more than 3 problems
Type 'Winner' to print out the winning team
Type 'Exit' to exit the program""")
    choice = input()
    choice = choice.lower()
    if choice == "insert team":
        loop = "no"
        ok = "no"
        while ok == "no":
            try:
                teamName, problems, time = input("Please give the team name the problems solved and the time it took in that order on a single line with spaces seperating them: ").split()
                problems = int(problems)
                time = float(time)
                ok = "yes"
            except:
                print("Invalid input returning to previous section")
                ok = "no"
            productList.insert_at_start(teamName, problems, time)
        ok = "no"
        loop = "yes"
        print(f"Team Name: {teamName} | Problems Solved: {problems} | Time Taken: {time}| Inserted into the list")
    elif choice == "print info":
        productList.traverse_list()
    elif choice == "average time":
        print(productList.getAverage())
    elif choice == "three problems":
        productList.lowStock()
    elif choice == "winner":
        print(productList.findPriceOfStuff(productList.getMax()))
    elif choice == "exit":
        print("""Goodbye, have a great day!
                Also, please consider giving this program an A+""")
        loop = "no"
    else:
        print("Invalid input returning to main menu")
        loop = "yes"


"""
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
    """
    

    





