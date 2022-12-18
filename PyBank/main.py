import os
import csv

# This sum function can process a list of numbers and add them up to return a total value
# Input List data_list
# Output Int total
def sum (data_list):
    total = 0
    for figure in data_list:
        total += figure
    return total

# This changes function can process a list of numbers and return a list of value difference between two consecutive numbers
# Input List data_list
# Output List diff
def changes(data_list):
    diff = [figure - data_list[data_list.index(figure)-1] for figure in data_list[1:]]
    return diff

# This readfile function will read through csv file with given path and skip the first header line, it returns a dictionary with all extracted data from the file
# Input filepath
# Output Dict bank_dict
def readfile(csv_path):
    date_list = []
    budget_list = []
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        headerrow = next(csvreader,None)
        for row in csvreader:
            date_list.append(row[0])
            budget_list.append(int(row[1]))

    bank_dict = {"date":date_list,"budget":budget_list}
    return bank_dict

# This writefile function will write given string into a output text file
# Input string results
# Output N/A
def writefile(results):
    output_path = os.path.join(".", "analysis","Result.txt")
    with open(output_path,"w") as textfile:
        textfile.write(results)

# Below is the main function of this project

# read and store the budget_data.csv file into a dictionary
bank_dict = readfile(os.path.join(".", "Resources","budget_data.csv"))

# get the date list from the dictionary
date_list = bank_dict["date"]

# get the budget list from the dictionary
budget_list = bank_dict["budget"]

# get the difference list from the budget list
change_list = changes(budget_list)

# calculate the total month
totalMonth = len(date_list)

# calculate the summation
totalBudget = sum(budget_list)

# calculate the average difference
averageChange = sum(change_list)/len(change_list)

# write the results to a text file
writefile(f'Financial Analysis\n---------------------------- \nTotal Months: {totalMonth} \nTotal: ${totalBudget} \nAverage Change: ${round(averageChange,2)} \nGreatest Increase in Profits: {date_list[change_list.index(max(change_list))+1]} (${max(change_list)})\nGreatest Decrease in Profits: {date_list[change_list.index(min(change_list))+1]} (${min(change_list)})')

# print the results to the terminal
print(f'Financial Analysis\n---------------------------- \nTotal Months: {totalMonth} \nTotal: ${totalBudget} \nAverage Change: ${round(averageChange,2)} \nGreatest Increase in Profits: {date_list[change_list.index(max(change_list))+1]} (${max(change_list)})\nGreatest Decrease in Profits: {date_list[change_list.index(min(change_list))+1]} (${min(change_list)})')