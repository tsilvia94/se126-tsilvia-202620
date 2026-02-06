#Midterm

#PROGRAM PROMPT
#Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold a student ID value for each student. The first student in the file should have an ID of 10001, each student’s ID should be unique, and the ID values should not exceed 10021. Once the new list is populated, process through the five lists to display all of the student data to the user as well as the total number of records in the file.


#VARIABLE DICTIONARY
#total_records          Total Number of Students
#first_name             Students first name
#last_name              Students last name
#department             Departnemts
#gpa                    Students GPA
#student_id             Students ID Number

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------

#--MAIN EXECUTING CODE------------------------------

#initalize known or needed values (counting vaiables)

total_records = 0       #in future can use: len(listName) to get length

#working with lists - 1 list for EACH POTENTIAL FIELDS in the data file

first_name = []   #create an empty list
last_name = []
department = []
gpa = []

print(f"{'Student ID' :13}{'FIRST':12}  {'LAST':12}  {'DEPT':7} {'GPA' :5} ")
print("-----------------------------------------------------------------------------")

#connect to file
with open ("students.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:

        #Rec[0] = First Name
        first_name.append(record[0])

        #Rec[1] =Last Name
        last_name.append(record[1])
       
        #rec[2]= department
        department.append(record[2])

        #rec[3] = gpa
        gpa.append(float(record[3]))

#disconnect from file

student_id = [] #create new list for student IDs


for i in range(0,len(first_name)):
    student_id.append(10001 + i)

for i in range(0, len(first_name)):
    print(f"{student_id[i]:<12} {first_name [i]:12}  {last_name [i]:12}  {department [i]:6} {gpa [i] :5.2f}")
print("-----------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(first_name)}")


#write student data file
file = open ("midterm_choice3.csv", "w")

for i in range(0, len(first_name)):
   file.write(f"{student_id[i]}, {first_name [i]}, {last_name [i]}, {department [i]}, {gpa [i]}")
file.close()


#Repeatable search
print("\tWelcome to the Student Seach Program!")

answer = input("Would you like to start your search? (y/n): ").lower()

while answer != "y" and answer != "n":
    print("\t!INVALID ENTRY! Please enter y or n.") 
    answer = input("Would you like to search again? [y/n]: ").lower() 

while answer == "y":

    print("\t~Search Menu~")
    print("1. Search by LAST name")         #one search value found
    print("2. Search by DEPARTMENT")      #multiple search values found
    print("3. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-3]: ")

    #filter search options based on type
    if search_type == "1": #LAST NAME    
        print("\tLAST NAME SEARCH")    
        found = -1 
        search_last = input("Enter the last name you wish to find: ") 
        for i in range(0, len(last_name)):
            if search_last.lower() == last_name[i].lower():
                found = i 

        if found != -1:
            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{student_id[found]:<12} {first_name [found]:12}  {last_name [found]:12}  {department [found]:6} {gpa [found] :5.2f}")
            
        else: 
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
    
    elif search_type == "2": #Department Search
        print("\tDEPARTMENT SEARCH")

        found = [] 
        search_department= input("Enter the  DEPARTMENT you wish to find: ") 
        for i in range(0, len(department)):
            if search_department.upper() == department[i]: 

                found.append(i)
                

        if not found: 
            print(f"Your search for {search_department} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            print(f"Your search for {search_department} was FOUND! Here is their data: ")

            for i in found: 
                print(f"{student_id[i]:<12} {first_name [i]:12}  {last_name [i]:12}  {department [i]:6} {gpa [i] :5.2f}")
    elif search_type == "3":
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    if search_type == "1" or search_type == "2":
        answer = input("Would you like to search again? [y/n]: ").lower()
    
    while answer != "y" and answer != "n":
        print("\t!INVALID ENTRY! Please enter y or n.") 
        answer = input("Would you like to search again? [y/n]: ").lower()  


print("\nThanks for using the search program. Goodbye!\n")