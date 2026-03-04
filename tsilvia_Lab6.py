#Tyler Silvia
#Lab 6
#3/3/2026

#PROGRAM PROMPT
#Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small airplane with seat numbering as follows.

#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------

#--FUNCTIONS----------------------------------------

#--MAIN EXECUTING CODE------------------------------
#7 Rows : 1 - 7
#4 seat types: A, B, C , D
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

#print the seat map!
for i in range (0, 7):
    print(f"{i + 1}  {seatA[i]}  {seatB[i]}     {seatC[i]}  {seatD[i]}")

#ask user for ROW : 1 - 7
row = int(input("Enter your desired ROW [1-7]: "))

#ask user for seat: A, B, C, D
seat = input("Enter your desired SEAT [A/B/C/D]: ")

#check seat and replace with X to reserve alert user if not
again = "y"

while again.lower() == "y":
    # ask user for seat
    row = int(input("Enter row number (1–7): "))
    seat = input("Enter seat letter (A–D): ").upper()

    if seat == 'A':
        if seatA[row - 1] != "X":
            seatA[row - 1] = "X"
        else:
            print(f"Sorry, seat {row}{seat} is already taken.")

    elif seat == 'B':
        if seatB[row - 1] != "X":
            seatB[row - 1] = "X"
        else:
            print(f"Sorry, seat {row}{seat} is already taken.")

    elif seat == 'C':
        if seatC[row - 1] != "X":
            seatC[row - 1] = "X"
        else:
            print(f"Sorry, seat {row}{seat} is already taken.")

    elif seat == 'D':
        if seatD[row - 1] != "X":
            seatD[row - 1] = "X"
        else:
            print(f"Sorry, seat {row}{seat} is already taken.")

    else:
        print(f"Sorry, seat {row}{seat} is not a valid seat.")

    # reprint seating chart
    print("\nCurrent seating:")
    for i in range(7):
        print(f"{i+1}  {seatA[i]}  {seatB[i]}     {seatC[i]}  {seatD[i]}")
        
    again = input("\nWould you like to choose another seat? (y/n): ")



