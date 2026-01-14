#Tyler Silvia
#Lab 1
#1-6-2025 [W1D2]

#PROGRAM PROMPT: You will be writing one Python file for this project - it is a program that determines whether ameeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending themeeting. If the number of people is less than or equal to the maximum room capacity, theprogram announces that it is legal to hold the meeting and tells how many additional people maylegally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowedto enter and check as many rooms as they would like without exiting the program 

#VARIABLE DICTIONARY
#diff       difference between max capacity and attendees
#decision   whether the user wants to continue using the program
#name       room name
#cap        room capacity
#attend     number of attendees
#
#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------
#function definition below - must define before calling the main code (using)
def difference (people, max_cap):

    diff = max_cap - people

    #the return value replaces the function call
    return diff #when diff < 0, too many people for the room

def decision(a):
    #error trap loops
    while a !="y" and a != "n":
        print ("*** INVALID ENTRY - 'y' or 'n' only! ")
        a = input("\t\tWould you like to enter check another room? [y/n]: ").lower()
    return a
    


#--------MAIN EXECUTING CODE----------------------------------
#function call below - actually the function
print("\n\t\t Welcome to my Lab #1")
answer = "y"

while answer == "y":
    #asks a user for the meeting name, room capacity, and people attending the meeting

    name = input("\nEnter the name of the room: ")
    cap = int(input(f"Enter the max capacity for {name} room: "))
    attend = int(input(f"Enter the number of people attending the meeting in {name} room: "))

    # passes the room capacity and people attending to the difference() you wrote in Part 1
    diff_return = difference (attend,cap)

    #displays to the user whether the meeting meets fire safety or not (legal/illegal) #also display how many people can be added or removed (remember: if different returns a negative number, this is how many people should be removed)   #NOTE: all values related to people (adding/removing) should be displayed as positive values   #- example: If the room capacity is 25 and 30 people are signed up for the meeting, the program should tell the user that “5 people must be removed from the meeting to meet fire regulations”; If the room capacity is 25 and 17 people are signed up for the meeting, the program should tell the user that “8 people can be added to the meeting and still meet fire regulations”
   
    if diff_return >= 0:
        print(f"The amount of people that you have attending is legal. You may add {diff_return} people.")
    else:
        print(f"The amount of people that you have attending is illegal. You need to remove {diff_return * -1} people.")
 
 
    #ask the user if they have another number to check; pass the value to the decision() you wrote in Part 2 and continue the program based on that function’s return

    answer = input("\t\t Would you like to check another room? [y/n]: ").lower()

    answer = decision(answer)

    #Once the user is done checking meeting attendance, display a goodbye message
print ("Thank you for using the program! Have a great day! ")