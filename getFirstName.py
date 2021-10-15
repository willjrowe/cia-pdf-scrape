import csv, re
from csv import reader

newMain = []

with open('main.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        newRow = row
        if row[5] == "Name": #handles header row
            newRow.append("First Name")
            newMain.append(newRow)
            continue
        fullName = row[5]
        firstName = fullName
        if firstName.find(",") > -1:
            firstName = firstName[0:firstName.find(",")] #remove anything after a ,
        if firstName.find("(") > -1: #remove anything between  (  )
            firstName = firstName[0:firstName.find("(")]
        firstName = re.sub(r'\b[A-Z]+\b', '', firstName) #remove uppercase string
        firstName = re.sub(r'\b[^\w\s]+', '', firstName)
        if fullName == "NA":
            firstName = "NA"
        if firstName.strip() == "": #when the only name is the last name
            firstName = "NA"
        firstName = firstName.strip()
        newRow.append(firstName)
        newMain.append(newRow)
        print(firstName)

with open('mainFirstNames.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newMain)