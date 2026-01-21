#W2 - Lab

#PROGRAM PROMPT
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#VARIABLE DICTIONARY

#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS----------------------------------------

#--MAIN EXECUTING CODE------------------------------

#initalize known or needed values (counting vaiables)

total_records = 0       #in future can use: len(listName) to get length

#working with lists - 1 list for EACH POTENTIAL FIELDS in the data file

m_type = []   #create an empty list
brand = []
cpu = []
ram = []
first_hd = []
num_hd = []
second_hd = []
os = []
yr = []

print(f"{'Type':10}{'Brand':10}{'Cpu':4}{'Ram':7}{'1st HD':7}{'#HD':5}{'2nd HD':7}{'OS':5}{'YR':5}")

#connect to file
with open ("filehandling.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:
        total_records += 1      #total_comp = total_comp + 1

        #Rec[0] = Machine Type
        if record[0] == "D":
            m_type.append("Desktop")
        elif record[0]:
            m_type.append("Laptop")
        else:
            m_type.append("*ERROR*")
       
        #Rec[1] =Brand
        if record[1] == "DL":
            brand.append("Dell")
        elif record[1] == "GW":
            brand.append("Gateway")
        elif record[1] == "HP":
            brand.append("HP")
        else:
            brand.append("*ERROR*")
             #all file data is read in as a string type
       
        #rec[2]= processor
        cpu.append(record[2])
       
        #rec[3] = ram
        ram.append(record[3])
        
        #rec[4] = 1st hard drive
        first_hd.append(record[4])
        
        #rec[5] - KEY TO RESET OF THE FIELDS! - num_hd
        if record[5] == "1":
            num_hd.append(record[5])
            second_hd.append("-----")         #no second hard drive
            os.append(record[6])
            yr.append (record[7])
        else:
            num_hd.append(record[5])
            second_hd.append(record[6])
            os.append(record[7])
            yr.append(record[8])

        #display machine data
        #print(f"{type:10}{brand:10}{cpu:4}{ram:7}{first_hd:7}{num_hd:5}{second_hd:7}{os:5}{yr:5}")
#print("-" * 50)
       
#PROCESS THROUGH THE LIST -- batch processing: do the same thing to each value in said list(s) -- for index in range (0, len(listName))
#                                                                                                 for index in listName
#PARALLEL LISTS : data organized in different lists, but connected via index
for index in range(0, len(m_type)):
    print(f"{m_type[index]:10}{brand[index]:10}{cpu[index]:4}{ram[index]:7}{first_hd[index]:7}{num_hd[index]:5}{second_hd[index]:7}{os[index]:5}{yr[index]:5}")
print("-" * 50)

old_desktops = 0
old_laptops = 0

for index in range(0, len(m_type)):
    #count desktops and laptops that are too old (year <= 16)
    if int(yr[index]) <= 16:
        #machine is too old - now determine type for proper counting
        if m_type[index] == "Desktop":
            old_desktops += 1
        elif m_type[index] == "Laptop":
            old_laptops += 1
        else:
            print(f"**** YOU HAVE AN ERROR IN Index / data file line: {index + 1}****")

print("\nMachines processed for replacement budget:")
print(f"Desktops to replace {old_desktops} @ $2k/each --> ${old_desktops * 2000:.2f}")
print(f"Laptops to replace {old_laptops} @ $1.5k/each --> ${old_laptops * 1500:.2f}")

total_cost = (old_desktops * 2000) + (old_laptops * 1500)
#disconnect from file

#display final values: total rooms counted, number of rooms over capacity