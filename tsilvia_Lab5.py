y#Tyler Silvia
#Lab 5
#2/14/2026

#PROGRAM PROMPT
#Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options. Your program should give your user the following menu: Personal Library Menu
#1. Show All Titles – list all book data to the user
#a. +10 bonus points if it is displayed alphabetically by title (and all other searches still work)
#2. Search by Title – allow for an entire title or a title key word – SEQUENTIAL SEARCH
#3. Search by Author – show all titles of the searched-for author – SEQUENTIAL SEARCH
#4. Search by Genre - show all titles of the searched-for genre – SEQUENTIAL SEARCH
#5. Search by Library Number – only allow for one specific library number item – BINARY SEARCH
#6. Show All Available – show all titles with status “available” – SEQUENTIAL SEARCH
#7. Show All On Loan - show all titles with status “on loan” – SEQUENTIAL SEARCH
#8. EXIT
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,cGenre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------
def swap(n, j):
    t = n[j]
    n[j] = n[j + 1]
    n[j + 1] = t

    return n[j], n[j + 1]
#--MAIN EXECUTING CODE------------------------------
total_records = 0

library_number = []
title = []
author = []
genre = []
page_count = []
status = []

with open ("book_list.csv") as csvfile:
    file = csv.reader(csvfile)
    for record in file:
        library_number.append(int(record[0]))
        title.append(record[1])
        author.append(record[2])
        genre.append(record[3])
        page_count.append(int(record[4]))
        status.append(record[5])


print(f"{'NUMBER':<10}{'TITLE':<40}{'AUTHOR':<20}{'GENRE':<20}{'PAGES':<10}{'STATUS':<10}")
print("-" * 110)
for i in range(0, len(library_number)):
    print(f"{library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")

#write student data file
file = open ("complied_book_info.csv", "w")

for i in range(0, len(library_number)):
   file.write(f"{library_number[i]},  {title[i]},  {author[i]} , {genre[i]},  {page_count[i]}, {status[i]}")
file.close()

#Repeatable search
print("\tWelcome to the Student Seach Program!")

answer = input("Would you like to start your search? (y/n): ").lower()

while answer == "y":

    print("\t~Search Menu~")
    print("1. Show all Titles")        #sequential
    print("2. Search by Title")        #sequential      
    print("3. Search by Author")       #sequeantial
    print("4. Search by Genre")        #sequential
    print("5. Search by Library Number")    #binary
    print("6. Show all Available")     #sequential
    print("7. Show all On Loan")       #sequential
    print("8. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-8]: ")

    #filter search options based on type
    if search_type == "1": #SHOW ALL TITLES    
        print(f"{'NUMBER':<10}{'TITLE':<40}{'AUTHOR':<20}{'GENRE':<20}{'PAGES':<10}{'STATUS':<10}")
        print("-" * 110)
        for i in range(0, len(library_number)):
            print(f"{library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")    
        
    elif search_type == "2": #SEARCH BY TITLE
        print(f"\t TITLE SEARCH")
        found = -1
        search_title = input("Enter the Title you wish to find: ")
        for i in range(0, len(title))   :
            if search_title.lower() == title[i].lower:
                found = i

        if found!= -1:
            print(f"Your search for {search_title} was FOUND! Here is the data: ")
            print(f"{library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")
        else:
            print(f"Your search for {search_title} was NOT FOUND!") 
        
    elif search_type == "3": #SEARCH BY AUTHOR
        print(f"\t AUTHOR SEARCH")
        found = -1
        search_author = input("Enter the Author you wish to find: ")
        for i in range(0, len(author))   :
            if search_author.lower() == author[i].lower:
                found = i

        if found!= -1:
            print(f"Your search for {search_author} was FOUND! Here is the data: ")
            print(f"{library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")
        else:
            print(f"Your search for {search_author} was NOT FOUND!")
            
    elif search_type == "4": #SEARCH BY genre
        print(f"\t GENRE SEARCH")
        found = -1
        search_genre = input("Enter the Genre you wish to find: ")
        for i in range(0, len(genre))   :
            if search_genre.lower() == genre[i].lower:
                found = i

        if found!= -1:
            print(f"Your search for {search_genre} was FOUND! Here is the data: ")
            print(f"{library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")
        else:
            print(f"Your search for {search_genre} was NOT FOUND!")

    elif search_type == "5": #SEARCH BY LIBRARY NUMBER
        print("\tLIBRARY NUMBER SEARCH")

        found = []
        search_lnum = input("Enter the Library Number you wish to find: ")
        for i in range(0, len(library_number)):
            if search_lnum == library_number[i]:
                found.append(i)
        
        if not found:
            print(f"Your search for {search_lnum} was NOT FOUND!")
        else:
            print(f" Your search for {search_lnum} was FOUND! Here is the data: ")

            for i in range(0, len(found)):
                print(f"{found[i]}:  {library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")


    elif search_type == "6": #SEARCH BY AVAILABLE
        print(f"\t GENRE SEARCH")
        found = -1
        search_genre = input("Enter the Genre you wish to find: ")
        for i in range(0, len(genre))   :
            if search_genre.lower() == genre[i].lower:
                found = i

        if found!= -1:
            print(f"Your search for {search_genre} was FOUND! Here is the data: ")
            print(f"{library_number[i]:<10}{title[i]:<40}{author[i]:<20}{genre[i]:<20}{page_count[i]:<10}{status[i]:<10}")
        else:
            print(f"Your search for {search_genre} was NOT FOUND!")

            for i in range(0, len(found)):
                print(f"{found[i]}:  {first_name[found[i]]:10}  {last_name[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {let_grade[found[i]]}")
    elif search_type == "3":
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    if search_type == "1" or search_type == "2":
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")