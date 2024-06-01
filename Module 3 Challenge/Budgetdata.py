#import modules
import csv
import os

# source to read budget data file
fileload = os.path.join("budgetData.csv")

# variables
totalMonths = 0 # intialize the total months to 0

# variables
totalMonths = 0 # intialize the total months to 0
totalBudget = 0 # intialize the total budget to 0
monthlyChanges = [] # intialize the list of monthly changes

# read the csv file 
with open(fileload) as budgetdata:
    #create a csv reader object
    csvreader = csv.reader(budgetdata)

    # read the header row
    header = next(csvreader)

    for row in csvreader:
    # increment the count of the total months
    totalMonths += 1 #same as totalMonths = totalMonths + 1

    # add on to the total amount of budget
        # budget is in index 1
        totalBudget += float(row [1])

    
   # start generating the output
    output = (
        f"\nBudget Data  \n"
        f"---------------------\n"
        f"\tTotal Months  = {totalMonths}"
    )
totalMonths += 1 #same as totalMonths = totalMonths + 1

    # print the output to the console / terminal
    print(output) 

# export the output to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)