#W2 - In Class Lab

#PROGRAM PROMPT
#The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.  Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------
def difference (people, max_cap):
    #this function is passed 2 values and returns the difference between them

    diff = max_cap - people
    return diff

#--MAIN EXECUTING CODE------------------------------

#initalize known or needed values (counting vaiables)

total_records = 0       #total records in file ->8
over_cap = 0            #total number of rooms over capacity ->3

print (f"{'ROOM NAME':20}  {'MAX':5}     {'PEOPLE':5}     {'REMOVE':5}")
print("-" * 50)
#connect to file
with open ("classLab2.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:
        total_records += 1      #total_records = total_records + 1

        #assign each field of data to a variable
        name = record[0]
        max = int(record[1])     #all file data is read in as a string type
        ppl = int(record[2])

        #call the difference() to find people over/under capacity
        remaining = difference (ppl, max)

        if remaining < 0:
            over_cap += 1
            print (f"{name:20}  {max:5}     {ppl:5}     {-remaining:5}")

#disconnect from file

#display final values: total rooms counted, number of rooms over capacity
print(f"\n\nROOMS OVER CAPACITY: {over_cap}\nTOTAL ROOMS in FILE: {total_records}")