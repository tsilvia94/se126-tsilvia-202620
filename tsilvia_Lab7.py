#Tyler Silvia
#Lab 7
#3/3/2026

#PROGRAM PROMPT
#Build a mini programming dictionary a user can search through and add to using the words.csv file:

#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------

#--MAIN EXECUTING CODE------------------------------

dictionary = {}

with open('words.csv') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dictionary.update({rec[0] : rec[1]})
        #rec[0] -> word = KEY, rec[1] -> definition

menu_choice = 0

while menu_choice != 4:
    print('\n\t My Programming Dictionary Menu')
    print("\t 1. Show all words")       #Show all words and their definitions stored to the dictionary
    print("\t 2. Search for a word")    #Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
    print("\t 3. Add a word")           # Allow a user to add a word and its definition to the dictionary if it does not already exist
    print("\t 4. EXIT")

    menu_choice = input("\tEnter your Choice [1-4]: ")

    if menu_choice == "1":
        for key in dictionary:
            print(f"\t{key.upper():15}: \n\t{dictionary[key]}")
    
    elif menu_choice == "2":
        found = 0
        search = input("\tEnter the WORD you are looking for: ")

        for key in dictionary:
            if key.upper() == search.upper():
                found = key
        if found != 0:
            print(f"\t{found.upper():15}: \n\t {dictionary[found]}")
        else:
            print(f"\tSorry, the {word} cannot be found")

                  
    elif menu_choice == "3":
        word = input("\tEnter the word you would like to add:")
        
        found = 0

        for key in dictionary:
            if key.upper() == word.upper():
                found = key
        if found == 0:
            print(f"\tOkay, I will add {word} to the Dictionary")
            defintion = input(f"\t Please enter the definition for {word}: ")

            dictionary.update({word : defintion})

            print(f"\t{found.upper():15}: \n\t {dictionary[found]}")
        else:
            print(f"\t Sorry, {word} already exists in the dictionary and cannot be added")
                  
    elif menu_choice == "4":
        print(f"\n\n Thank you for using my program!")
    else:
        print(f"\n\tSorry {menu_choice} os not a valid menu option. Please try again.\n")