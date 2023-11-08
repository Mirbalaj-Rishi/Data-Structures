import random

list = ["1", "2", "3"]
#rock scissors paper
U = "you win"
c = "The Computer Wins"
keepGoing = "y"

while keepGoing == "y": 
    userChoice = input("Press 1 for Rock, Press 2 for Scissors, Press 3 for Paper: ")
    com = random.choice(list)
    if com == "1":
        com2 = "rock"
    elif com == "2":
        com2 = "scissors"
    elif com == "3":
        com2 = "paper"
    
    print("The computer choose: ", com2) 

    if userChoice == com:
        print("It's a tie")

    elif userChoice == "1" and com == "2":
        print("rock crushes scissors")
        print(U)

    elif userChoice == "2" and com == "3":
        print("sicssors cuts paper")
        print(U)

    elif userChoice == "3" and com == "1":
        print("paper covers rock")
        print(U)

    elif userChoice == "1" and com == "3":
        print("paper covers rock")
        print(c)
    elif userChoice == "3" and com == "2":
        print("sicssors cuts paper")
        print(c)
    elif userChoice == "2" and com == "1":
        print("rock crushes scissors")
        print(c)
    else:
        print("You didn't type the correct thing")

    keepGoing = input("continue?  y or n: ")



    
    
    

