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

first_name = []   #create an empty list
last_name = []
test1 = []
test2 = []
test3 = []
num_avg =[]
let_grade =[]


print(f"{'FirstName':15}{'LastName':15}{'Test1':7}{'Test2':7}{'Test3':7}{'Average':8}{'Grade':6}")
print(f"-"*64)

#connect to file
with open ("class_grades-2.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each ' record' in 'file' (for loop)
    for record in file:
        total_records += 1      #total_comp = total_comp + 1

        #Rec[0] = First Name
        first_name.append(record[0])

        #Rec[1] =Last Name
        last_name.append(record[1])
       
        #rec[2]= Test 1
# convert test scores to integers
        t1 = int(record[2])
        t2 = int(record[3])
        t3 = int(record[4])

        test1.append(t1)
        test2.append(t2)
        test3.append(t3)

        # calculate average
        avg = (t1 + t2 + t3) / 3
        num_avg.append(avg)

        # determine letter grade
        let_grade.append(record[5])
        if avg >= 90:
            let_grade.append("A")
        elif avg >= 80:
            let_grade.append("B")
        elif avg >= 70:
            let_grade.append("C")
        elif avg >= 60:
            let_grade.append("D")
        else:
            let_grade.append("F")


#display Grdes
#prin(f"{'FirstName':10}{'LastName':9}{'Test1':6}{'Test2':6}{'Test3':6}{'Average':8}['Grade':6]")

       
#PROCESS THROUGH THE LIST -- batch processing: do the same thing to each value in said list(s) -- for index in range (0, len(listName))
#                                                                                                 for index in listName
#PARALLEL LISTS : data organized in different lists, but connected via index
for index in range(0, len(first_name)):
    print(f"{first_name[index]:15}{last_name[index]:15}{test1[index]:5}{test2[index]:7}{test3[index]:7}{num_avg[index]:9.2f}{let_grade[index]:9}")


#disconnect from file

#display final values: total rooms counted, number of rooms over capacity