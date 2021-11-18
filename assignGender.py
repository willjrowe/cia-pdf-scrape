import csv, re
from csv import reader

firstNameList = []
ga_first_name_list = []
ga_gender_list = []
ga_accuracy_list = []
ga_samples_list = []


#check if gender is male or female or unknown otherwise skip

with open('firstNameGenderKey.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[1] == "ga_first_name": #skips header row
            continue
        if row[2] == "male" or row[2] == "female" or row[2] == "unknown":
            firstNameList.append(row[0])
            ga_first_name_list.append(row[1])
            ga_gender_list.append(row[2])
            ga_accuracy_list.append(row[3])
            ga_samples_list.append(row[4])


newMain = []

with open('mainFirstNames.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        newRow = row
        if row[11] in firstNameList:
            index = firstNameList.index(row[11])
            newRow.append(ga_first_name_list[index])
            newRow.append(ga_gender_list[index])
            newRow.append(ga_accuracy_list[index])
            newRow.append(ga_samples_list[index])
        else:
            newRow.append("Not Found")
            newRow.append("Not Found")
            newRow.append("Not Found")
            newRow.append("Not Found")
        newMain.append(newRow)


with open('genderAssignTest.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newMain)