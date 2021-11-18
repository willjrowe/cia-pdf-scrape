import csv, re
from csv import reader

newMain = []

specialPre = ["bin ", "van ", "van de ", "van der ", "van den "]

firstNameList = []

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
        if firstName.lower().startswith(tuple(specialPre)):
            newRow.append(firstName)
            newMain.append(newRow)
            continue
        if firstName.upper() == firstName: #case for when string is already all caps, just leave first name
            if firstName != "NA" and firstName != "VACANT":
                if firstName.find(" ") > 0:
                    firstName = firstName[0:firstName.find(" ")]
                firstName = firstName.lower()
                firstName = firstName.capitalize()
                newRow.append(firstName)
                newMain.append(newRow)
                continue
        if firstName.find(",") > -1:
            firstName = firstName[0:firstName.find(",")] #remove anything after a ,
        if firstName.find("(") > -1: #remove anything between  (  )
            firstName = firstName[0:firstName.find("(")]
        firstName = re.sub(r'\b[A-Z]+\b', '', firstName) #remove uppercase string
        firstName = re.sub(r'\B[^\w\s]+\B', ' ', firstName)
        firstName = re.sub(r'[^\w\s]+\B', ' ', firstName) 
        firstName = re.sub(r'\B[^\w\s]', ' ', firstName)  
        if fullName == "NA":
            firstName = "NA"
        if fullName == "VACANT":
            firstName = "NA"
        if firstName.strip() == "": #when the only name is the last name
            firstName = "NA"
        firstName = firstName.strip()
        if firstName.lower() not in firstNameList:
            firstNameList.append(firstName.lower())
            newRow.append(firstName)
            newMain.append(newRow)


with open('justFirstNamesCode.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newMain)