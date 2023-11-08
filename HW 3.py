# imports important modules 
import array
import random


# This is the linear search code I got from the slides, I modified it to better fit my code
# I added a section that allows me to input both the number the user put in and the array that I want to use
# I also changed the outputs of the function 
def linearSearch(number,array):
    for n in array:
        if n==number:
            print("Linear Search says: Your number is in the array. :)")
            return 
    print("Linear Search says: Your number is not in the array. :(")
    return

# This is the binary search code I got from the slides, I modified it to better fit my code
# I added a section that allows me to input both the number the user put in and the array that I want to use
# I also changed the outputs of the function
def BinarySearch(number, array):
    l =0
    r = len(array) - 1
    while (l <= r):
        m = ( l+r )// 2
        if (array[m] == number):
            print("Binary Search says: Your number was found in the array at location,",m)
            return 1
        elif (array[m] < number):
            l = m + 1
        else :
            r = m - 1
    # if we reach here, then element was not present
    print("Binary Search says: Your number wasn't found in the array. :(")
    return -1
    



#This code generates an array by appending a random number to the end of the array 5000 times.
randomNumberArray = array.array("i",[])
for r in range(0,5000):
    r = random.randint(0,20001)
    randomNumberArray.append(r)

#this sorts the array
randomNumberArrayThatIsSorted = sorted(randomNumberArray)      

# This prints out the array along with a message labling the array. 
print("Here is an array that is filled with randomly generated numbers.")
print(randomNumberArray)
print("\n Here is that same array but sorted.")
print(randomNumberArrayThatIsSorted)



# this code uses a variable called workAround in order to keep the code looping until the user puts a correct imput
workAround = -1 
while workAround == -1:
    # this try and except code checks to make sure that the user's input can actually be turned into an integer
    try:
        askUser = int(input("Pick a number between 0 - 20,000 and type it here: "))
        # this code checks to make sure that the users input actually ranges from 0 - 20,000
        if not askUser >= int(0) or not askUser <= int(20000):
            workAround = -1
            print("Sorry your number must be between 0 - 20,000")
        else:
            workAround = 1
    except:
        workAround = -1
        print("Sorry, input invalid. Please only input a number between 0 - 20000, also don't include a comma or decimal in your responses")

# This takes the user's input and uses a linear search to find it in an array.
# it makes use of the linearSearch function from before. 
linearSearch(askUser,randomNumberArrayThatIsSorted)


# This takes the user's input and uses a binary search to find it in an array
BinarySearch(askUser,randomNumberArrayThatIsSorted)






