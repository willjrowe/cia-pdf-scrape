import csv

file = open("cleanedMarch2020ChiefsDirectory.txt","r")

txt = file.readlines()
# exit()

currCountry = None
foundRole = False
currRole = None
nextLine = None

main = []

i = 0

while i < len(txt):
    currLine = txt[i]
    if i < len(txt) - 1:
        nextLine = txt[i+1]
    bytesArr = bytes(currLine, 'utf-8')

    #Check special character
    if bytesArr[0] == 12 and ("Last Updated:" in nextLine):
        currCountry = currLine[1:].strip()
        currUpdated = nextLine[14:].strip()
    elif currLine.strip() == "" or ("Last Updated:" in currLine):
        pass
    #We know content on line
    else:
        if nextLine.strip() == "": #this is the normal case
            currRole = currLine.strip()
            currName = txt[i+2].strip()
            currStatus = "Titular"
            if "ACTING" in currName.upper() or "ACTING" in currRole.upper():
                currStatus = "Acting"
            if "INTERIM" in currName.upper() or "INTERIM" in currRole.upper():
                currStatus = "Interim"
            if i < len(txt) - 3 and "Last Updated:" in txt[i+3]: #weird edge case when last role from page before is empty
                currName = "NA"
                i-=1
            currRow = [
                currCountry, #country
                "2020", #document year
                "March", #document month
                "NA", #branch
                currRole, #position
                currName, #name
                currStatus, #status
                "NA", #gender
                "March2020ChiefsDirectory.pdf", #file
                currUpdated, #CIA last updated
                "10/13/2021 03:35", #when this script was run
            ]
            main.append(currRow)
            i+=2
        else: #no name skip 
            currRole = currLine.strip()
            currName = "NA"
            currStatus = "Titular" #always titular in this case
            currRow = [
                currCountry, #country
                "2020", #document year
                "March", #document month
                "NA", #branch
                currRole, #position
                currName, #name
                currStatus, #status
                "NA", #gender
                "March2020ChiefsDirectory.pdf", #file
                currUpdated, #CIA last updated
                "10/13/2021 03:35", #when this script was run
            ]
            main.append(currRow)
    i+=1



with open('March2020.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(main)