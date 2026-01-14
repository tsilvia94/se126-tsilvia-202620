#W2 - Text File Handling Intro Demo

#Step 1 - Import from csv
import csv

total_records = 0 #holds total num of recs in file

#Step 2 - connect to file
#--connected to file ------------------------------
#include relative file path in () - make sure to switch \ to /
with open("simple.csv") as csvfile:
    #make sure to indent inside of code block!

    #allow csv reader to access and read the file
    file = csv.reader(csvfile)
    #file = entire data from file! Organized as records

    #Step 3 - process through every record in the file
    for record in file:
        #add +1 to total_records to keep accurate count
        total_records += 1 #total_records = total_records + 1

        #print(record)   #entire record data as a list

        name = record[0]    #name field
        number = record[1]  #number field
        color = record[2]   #color field
        
        print(f"{name}'s number is {number} and they love the color {color}!")


#--disconnected from file------------------------------
print("----------------------------------")
print(f"\nTOTAL RECORDS: {total_records}\n")