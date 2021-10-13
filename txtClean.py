read_file = input("Enter txt file to clean: ")

write_file = open("cleaned" + read_file,"w")
read_file = open(read_file,"r")

txt = read_file.readlines()

i = 0
pageCount = 1
firstCountryFound = False

autoDelete = ["National Govt.",
            "Federation Govt.",
            "Republika Srpska Govt.",
            "Hong Kong (Special Admin. Region of the People's Republic of China)",
            "Macau (Special Admin. Region of the People's Republic of China)",
            "Powered by TCPDF (www.tcpdf.org)",
            ]

while i < len(txt):
    currLine = txt[i]
    if currLine.strip() not in autoDelete:
        if i < len(txt) - 1:
            nextLine = txt[i+1]
        bytesArr = bytes(currLine,'utf-8')
        if bytesArr[0] == 12:
            pageCount+=1
        if firstCountryFound == False: #cut out everything before the first country
            if bytesArr[0] == 12 and ("Last Updated:" in nextLine):
                firstCountryFound = True
                write_file.write(currLine)
        else:
            if (not currLine.strip() ==  "" and not nextLine.strip() == "" and "Last Updated:" not in nextLine):
                print("Back to back text lines detected!")
                print("Current Page: " + str(pageCount))
                print(currLine.strip())
                print(nextLine.strip())
                validInput = False
                while not validInput:
                    shouldCombine = input("Combine these into a single line? y or n?")
                    if shouldCombine == "y" or shouldCombine == "n" or shouldCombine == "d":
                        validInput = True
                if shouldCombine == "y":
                    write_file.write(currLine.strip() + " " + nextLine.strip() + "\n")
                    i+=1
                elif shouldCombine == "d":
                    i+=2
                else:
                    write_file.write(currLine)
            else:
                write_file.write(currLine)
    i+=1