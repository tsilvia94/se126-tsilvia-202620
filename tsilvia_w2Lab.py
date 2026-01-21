#W2 - Lab

#PROGRAM PROMPT
#You have been asked to produce a report that lists all the computers in the csv file filehandling.csv.  Your report should look like the following sample output. The last line should print the number of computers in the file.


#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------

#--MAIN EXECUTING CODE------------------------------

#initalize known or needed values (counting vaiables)

total_records = 0       #total comp in file ->29

print (f"{'Type':10}{'Brand':10}{'CPU':4}{'RAM':7}{'1st HD':7}{'#HD':5}{'2nd HD':7}{'OS':5}{'Yr':5}")

#connect to file
with open ("filehandling.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:
        total_comp += 1      #total_comp = total_comp + 1

        #Rec[0] = Machine Type
        if record[0] == "D":
            type = "Desktop"
        elif record[0]:
            type = "Laptop"
        else:
            type = "*ERROR*"
       
        #Rec[1] =Brand
        if record[1] == "DL":
            brand = "Dell"
        elif record[1] == "GW":
            brand = "Gateway"
        elif record[1] == "HP":
            brand = "HP"
        else:
            brand = "*ERROR*"
             #all file data is read in as a string type
       
        #rec[2]= processor
        cpu = record[2]
       
        #rec[3] = ram
        ram = record[3]
        
        #rec[4] = 1st hard drive
        first_hd = record[4]
        
        #rec[5] - KEY TO RESET OF THE FIELDS! - num_hd
        if record[5] == "1":
            num_hd = record[5]
            second_hd = "-----" #no second hard drive
            os = record[6]
            yr = record[7]
        else:
            num_hd = record[5]
            second_hd = record[6]
            os = record[7]
            yr = record[8]

        #display machine data
        print(f"{type:10}{brand:10}{cpu:4}{ram:7}{first_hd:7}{num_hd:5}{second_hd:7}{os:5}{yr:5}")
       

       

#disconnect from file

#display final values: total rooms counted, number of rooms over capacity
print(f"\n\nTotal Number of Computers: {total_records}")