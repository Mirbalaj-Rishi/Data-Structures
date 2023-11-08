# this asks for and stores the user input
userImput = input("Please, input your equation: ")
# this ensures that the program only displays correct when there are no problems found
allClear = "yes for now"
# this for loop stores only the parentheses, brackets, and culy brackts in the list

list = []
for i in userImput:
    if i == "(" or i == ")" or i == "[" or i == "]" or i == "{" or i == "}":
        list.append(i)
#this checks to see if there are no parentheses, brackets, and culy brackts in the list
# if there are none, then it displays prints out a message and sets allClear to "no contest" in order to prevent it printing out correct later on
if list == []:
    print("No parentheses, brackets, or culy brackets found.")
    allClear = "no contest"

# This is where the computer checks if the parentheise are ok
while list != []:
    if list[0] == "(" or list[0] == "{" or list[0] == "[":
        # The program works by removeing items from both sides of the list
        # is this ok?
        if list[0] == "(" and list[-1] == ")":
            list.pop(0)
            list.pop(-1)
        elif list[0] == "[" and list[-1] == "]":
            list.pop(0)
            list.pop(-1)
        elif list[0] == "{" and list[-1] == "}":
            list.pop(0)
            list.pop(-1)
        # this will let the user know if a parentheses, bracket, or curly bracket is left open
        elif list[0] == list[-1]:
            print("ERROR, parentheses opened but never closed")
            allClear = "no"
            break
        # this checks to see if something is mismatched
        elif list[0] == "(" and list[-1] != ")":
            print("ERROR, mismatched parentheses ")
            allClear = "no"
            break
        # Do I need to change this to say mismatched bracket? 
        elif list[0] == "[" and list[-1] != "]":
            print("ERROR, mismatched parentheses ")
            allClear = "no"
            break
        # Do I need to change this to say mismatched curly bracket? 
        elif list[0] == "{" and list[-1] != "}":
            print("ERROR, mismatched parentheses ")
            allClear = "no"
            break
    elif list[0] == ")" or list[0] == "}" or list[0] == "]":
        print("ERROR, parentheses closed but never opened")
        allClear = "no"
        break

# this is what the allClear variable is used for
# to make sure that the program only prints CORRECT if all the checks from before work
if allClear == "yes for now":
    print("CORRECT")


        
