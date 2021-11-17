# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Sheri Elgin, Nov 15, 2021, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    f = open(objFile,"r")
    for row in f:
        dicRow = row.split(",")
        dicRow = {"Task": dicRow[0], "Priority": dicRow[1].strip()}
        lstTable.append(dicRow)
    f.close()
except:
    print('Unable to open/read source file')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # Show current data in lstTable
        print("Task     \t" + " | \t" + "Priority")
        for dicRow in lstTable:
            print(dicRow["Task"] + " | \t" + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Add a task
        usrTask = input("Please enter a task you wish to add: ")
        usrPri = input("What priority level (1-3) do you want to assign it? ")
        dicRow = {"Task": usrTask, "Priority": usrPri}
        lstTable.append(dicRow)
        print("Added task " + usrTask + " as priority " + usrPri + "\n")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # remove an item from list
        usrRemove = input("Which item do you wish to remove? ")
        for row in lstTable:
            if row["Task"].lower() == usrRemove.lower():
                lstTable.remove(row)
        print("Removed task " + usrRemove + "\n")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # save list data to file
        try:
            f = open(objFile, "w")
            for row in lstTable:
                f.write(str(row["Task"]) + "," + str(row["Priority"] + "\n"))
            print("Saved data to file")
            f.close()
        except:
            print('Unable to open/write to source file')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # quit program
        print("Exiting program, goodbye.")
        break
