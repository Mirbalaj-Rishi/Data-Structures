# use 8009 for hash size
hash = 8009
list = []
for i in range(hash):
    list.append([])

ended = "no"

print("""
Welcome to My Homework 7 Hash Table Code.
    *Now With An Improved Menu!
""")

while ended == "no":
    # menu
    print("")
    choice = input("""
Please press 1 to add something to the Hash Table.
Please press 2 to print out the Hash Table.
Please press 3 to find something in the Hash Table.
Please press 4 to delete something from the Hash Table.
Please press 5 to end the program.

""")
    print("")
    
    # adding stuff into the Hash Table
    if choice == "1":
        worked = "no"
        while worked == "no":
            try:
                userInput = int(input("please type in the student number you want to add: "))
                worked = "yes"
            except:
                print("")
                print("Invalid input returning to the previous section.")
                print("")
                worked = "no"
        print("")
        hashCode = userInput % hash
        list[hashCode].append(userInput)
        print(f"{userInput} successfully added into the Hash Table")

# printing the Hash Table

    elif choice == "2":
        print("Location| Student Number")
        print("--------|---------------")
        for i in range(hash):
            print(f"{i} \t| {list[i]}")
        print("")





# finding stuff in the Hash Table

    elif choice == "3":
        found = "no"
        worked = "no"
        while worked == "no":
            try:
                userInputFind = int(input("please type in the student number you want to find: "))
                worked = "yes"
            except:
                print("")
                print("Invalid input returning to the previous section.")
                print("")
                worked = "no"
        hashCode = userInputFind % hash
        print("")
        for i in list[hashCode]:
            if i == userInputFind:
                print("FOUND IT!")
                found = "yes"
        if found == "no":
            print("Sorry the number you are trying to reach has not been found.")


# deleting stuff from the Hash Table

    elif choice == "4":
        found2 = "no"
        worked2 = "no"
        while worked2 == "no":
            try:
                userInputDelete = int(input("please type in the student number you want to delete: "))
                worked2 = "yes"
            except:
                print("")
                print("Invalid input returning to the previous section.")
                print("")
                worked2 = "no"
        hashCode = userInputDelete % hash
        print("")
        for i in list[hashCode]:
            if i == userInputDelete:
                list[hashCode].remove(i)
                print(f"{userInputDelete} has been removed from the Hash Table")
                found2 = "yes"
        if found2 == "no":
            print("The number you tried to delete wasn't in the Hash Table to begin with, did you delete it already?")

# ending the program 

    elif choice == "5":
        ended = "yes"
        print("Bye, have a great day!")
        print("")
        print("Also, please consider giving this program an A+")
        print("")

# just in case the user types in the wrong input
    else:
        print("Invalid input returning to the previous section.")
