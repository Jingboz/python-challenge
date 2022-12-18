import os
import csv

# This readfile function will read through csv file with given path and skip the first header line, 
# and it returns a dictionary with a list of unrepeatable candidate names and a list of names in the poll 
# Input filepath
# Output Dict name_dict
def readfile(csv_path):
    name_set = set()
    full_list = []
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        headerrow = next(csvreader,None)
        for row in csvreader:
            name_set.add(row[2])
            full_list.append(row[2])
        name_list = list(name_set)
        name_list.sort()
        name_dict = {"name":name_list, "full":full_list}
    return name_dict

# This count founction is for counting how many votes each candidate gets
# Input list components: a list of unrepeatable candidate names
# Input list dataset_list: the list of the whole poll
# Output list count_list
def count(components, dataset_list):
    count_list = [0]*len(components)
    for item in dataset_list:
        count_list[components.index(item)] += 1 
    return count_list

# This sum function can process a list of numbers and add them up to return a total value
# Input List data_list
# Output Int total
def sum (data_list):
    total = 0
    for figure in data_list:
        total += figure
    return total

# This writefile function will write given string into a output text file
# Input string results
# Output N/A
def writefile(results,mode):
    output_path = os.path.join(".", "analysis","Result.txt")
    with open(output_path,mode) as textfile:
        textfile.write(results)


# Blow is the main function of this project
# 
name_dict = readfile(os.path.join(".", "Resources","election_data.csv"))
count_list = count(name_dict["name"],name_dict["full"])

# write the results to a text file
writefile(f'Election Results\n-------------------------\nTotal Votes: {sum(count_list)}\n-------------------------\n',"w")

for index in range(len(count_list)):
    writefile(f'{name_dict["name"][index]}: {round(count_list[index]/sum(count_list)*100,3)}% ({count_list[index]})\n',"a")

writefile(f'-------------------------\nWinner: {name_dict["name"][count_list.index(max(count_list))]}\n-------------------------',"a")

# print the results to the terminal
print(f'Election Results\n-------------------------\nTotal Votes: {sum(count_list)}\n-------------------------')

for index in range(len(count_list)):
    print(f'{name_dict["name"][index]}: {round(count_list[index]/sum(count_list)*100,3)}% ({count_list[index]})')

print(f'-------------------------\nWinner: {name_dict["name"][count_list.index(max(count_list))]}\n-------------------------')