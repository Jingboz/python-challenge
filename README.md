Two python projects have been uploaded separately

PyBank: 

The functions are implemented to this project includes
sum (data_list), changes(data_list), readfile(csv_path), writefile(results)
For more details of the parameters please refer to the comments.

The program will first read the file using readfile() from given folder and store the data in a dictionary. And then generating the list of difference between two consecutive numbers from the budget column in the original dataset, which means the capacity of the difference list is one element less than the original one. So when we calculate the greatest increase/decrease months, we can't get the index from the difference list and directly apply to the original one, the index needs to plus one to indicate the former month after changes. Finally, the messages will be written to the file via writefile(), and printed to the terminal with print()

-------------------------------------------

PyPoll:

The functions are implemented to this project includes
sum (data_list), count(components, dataset_list), readfile(csv_path), writefile(results)
For more details of the parameters please refer to the comments.

The program will first read the file using readfile() from given folder and store the data in a dictionary, which contains a list of unrepeatable candidate names and a full name list of the poll. Note I used the property of set() to avoid any duplicated values when creating the unrepeatable name list. These two lists will be passed into count() to generate the voting result of each candidate. This count() function goes through all names in the poll and put the vote in a new count_list with the corrsponding name index in the unrepeatable name list. After all usefull data is extracted, we could use the writefile() and print() to write the result to a new file and terminal respectively.