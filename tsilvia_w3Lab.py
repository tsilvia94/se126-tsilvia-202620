#W3 - Lab

#PROGRAM PROMPT
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------

#--MAIN EXECUTING CODE------------------------------

#initalize known or needed values (counting vaiables)

total_records = 0       #in future can use: len(listName) to get length
not_eligible = 0
num_registered = 0
not_registered = 0
didnt_vote = 0
did_vote = 0

#working with lists - 1 list for EACH POTENTIAL FIELDS in the data file

id_number = []   #create an empty list
age = []
registered = []
voted = []

print(f"{'ID':7}{'Age':4}{'Registration':13}{'Voted':6}")

#connect to file
with open ("voters_202040.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:
        total_records += 1      #total_comp = total_comp + 1

        #Rec[0] = ID Number
        id_number.append(record[0])
       
        #Rec[1] = Age
        age.append(record[1])
           
        #rec[2]= Registered
        registered.append(record[2])
       
        #rec[3] = Voted
        voted.append(record[3])
        
        #display machine data
        #print(f"{id_number:10}{age:10}{registered:4}{voted:7}")
#print("-" * 50)
       
#PROCESS THROUGH THE LIST -- batch processing: do the same thing to each value in said list(s) -- for index in range (0, len(listName))
#                                                                                                 for index in listName
#PARALLEL LISTS : data organized in different lists, but connected via index
for index in range(0, len(id_number)):
    print(f"{id_number[index]:7}{age[index]:4}{registered[index]:13}{voted[index]:5}")
print("-" * 50)

old_desktops = 0
old_laptops = 0

for index in range(0, len(id_number)):
   
    if int((age[index])) < 18:
            not_eligible += 1

    if (registered[index]) == "N" and int((age[index])) >= 18:
         not_registered += 1
         
    if (voted[index]) == "Y":
        did_vote += 1
    else:
        didnt_vote += 1

print(f"The Number of inelgible voters is: {not_eligible}")
print(f"The Number of Voters not registered: {not_registered}")
print(f"The Number of Voters who are registered and voted: {did_vote}")
print(f"The Number of Voters who did not vote: {didnt_vote}")
print(f"Total number of Voters: {total_records}")
#disconnect from file

#display final values: total rooms counted, number of rooms over capacity