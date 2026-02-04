#W2 - Lab

#PROGRAM PROMPT
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------
def letter(a):
 
    if a >= 90:
        let = "A"
    elif a >= 80:
        let = "B"
    elif a >= 70:
        let = "C"
    elif a >= 60:
        let = "D"
    elif a < 60:
        let ="F"
    else:
        let = "ERROR"
    return let
#--MAIN EXECUTING CODE------------------------------

#initalize known or needed values (counting vaiables)

total_records = 0       #in future can use: len(listName) to get length

#working with lists - 1 list for EACH POTENTIAL FIELDS in the data file

first_name = []   #create an empty list
last_name = []
test1 = []
test2 = []
test3 = []



print(f"{'FIRST':10}  {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("-----------------------------------------------------------------------------")

#connect to file
with open ("class_grades-2.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:

        #Rec[0] = First Name
        first_name.append(record[0])

        #Rec[1] =Last Name
        last_name.append(record[1])
       
        #rec[2]= Test 1
        test1.append(int(record[2]))

        #rec[3] = Test 2
        test2.append(int(record[3]))

        #rec[4] = Test 3
        test3.append(int(record[4]))

#disconnect from file

num_avg = []
let_grade = []

for i in range(0,len(first_name)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_grade.append(letter(a))



for i in range(0, len(first_name)):
    print(f"{first_name[i]:10}  {last_name[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.1f}  {let_grade[i]}")
print("-----------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(first_name)}")


#write student data file
file = open ("complied_class_info.csv", "w")

for i in range(0, len(first_name)):
   file.write(f"{first_name[i]},  {last_name[i]},  {test1[i]} , {test2[i]},  {test3[i]}, {num_avg[i]},  {let_grade[i]}")
file.close()


#Repeatable search
print("\tWelcome to the Student Seach Program!")

answer = input("Would you like to start your search? (y/n): ").lower()

while answer == "y":

    print("\t~Search Menu~")
    print("1. Search by LAST name")         #one search value found
    print("2. Search by LETTER grade")      #multiple search values found
    print("3. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-3]: ")

    #filter search options based on type
    if search_type == "1": #LAST NAME    
        print("\tLAST NAME SEARCH~")    
        found = -1 
        search_last = input("Enter the last name you wish to find: ") 
        for i in range(0, len(last_name)):
            if search_last.lower() == last_name[i].lower():
                found = i 

        if found != -1:
            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{first_name[found]:10}  {last_name[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_grade[found]}")
        else: 
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
    
    elif search_type == "2": #LETTER GRADE
        print("\tLETTER GRADE SEARCH")

        found = [] 
        search_let= input("Enter the LETTER GRADE you wish to find: ") 
        for i in range(0, len(let_grade)):
            if search_let.upper() == let_grade[i]: 

                found.append(i)
                

        if not found: 
            print(f"Your search for {search_let} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

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