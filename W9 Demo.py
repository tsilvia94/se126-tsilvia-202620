#Dictionaries: another collection type in Python (like lists)


import csv

#dictionary -> {}
library = {
    #indexes are STRINGS set by the developer
    #'KEY' : value,
    '1230' : "Red Rising",
    '1231' : "The Little Prince"
}

#print(f"library['1230']: {library['1230']}")

#lists -> []
lib_nums = []
    #'1234',  #--> [0]
    #'1235'   #--> [1]
#]
titles = []
#print(f"lib_nums[0]: {lib_nums[0]}")  #--> '1234'


with open('dictionary_file-1.csv') as csvfile:
    file = csv.reader (csvfile)

    for rec in file:
        lib_nums.append(rec[0])
        titles.append(rec[1])
        #add each record's data as a new KEY + VALUE pair from the text file
        #key --> rec[0], value --> rec[1]
        library.update({rec[0] : rec[1]})
#disconnect from file--------------------------------------------------------

print (f"\n---PRINTING FROM LISTS----------------")
print(f"\n{'LIBRARY NUM'}\t{'TITLE'}")
print("-" * 50)
for i in range (0, len(titles)):
    print (f"{lib_nums[i]:11}\t{titles[i]}")

print("-" * 50)

print (f"\n---PRINTING FROM DICTIONARY----------------")
print(f"\n{'KEY':6}\t{'VALUE'}")
print("-" * 50)
for key in library:
    #for every key in our library dictionary
    print (f"{key:6}\t{library[key]}")

print("-" * 50)

#SEQUENTIAL SEARCH FOR A  - using dictionary

search = input("\nEnter the TITLE you are looking for:")
found = 0 #bc were using a dictionary! Keys will never be numbers! always strings!

for key in library:
    if search.lower() == library[key].lower():
        #store the found titles location
        found = key
if found != 0:
    print(f"\nKEY: {found} \t TITLE: {library[found]}")
else:
    print(f"\nYour search or {search} came up empty")


#BINARY SEARCH FOR A LIBRARY NUM - using LISTS!

min = 0 #reps the first possible index
max = len(titles) - 1 #reps the last possible index
mid = int(min + max / 2)
                    #// FLOOR --> removes the decimal
search = input ("\n Enter the LIBRARY NUM you are looking for: ")

while min < max and search != lib_nums[mid]:
    if search < lib_nums[mid]:
        max = mid - 1
    else:
        min = mid + 1

    mid = int(min + max / 2)
if search == lib_nums[mid]:
    print(f"\nINDEX: {mid} \t TITLE: {titles[mid]}")
else:
    print(f"\nYour search or {search} came up empty")
