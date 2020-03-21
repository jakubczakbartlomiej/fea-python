import os

# GLOBAL VARIABLES #
youngX = []
poissonXY = []
node = []
####################

def loadInputFile():
    os.system('cls')
    testFilesList = os.listdir("testfiles")
    i = 1
    for specificFile in testFilesList:
        print(str(i) + ".  " + str(specificFile))
        i += 1
    userChoice = input("Which file would you like to use? (insert number and press ENTER): ")
    return testFilesList[int(userChoice)-1]

def checkElementType(inputFilename):
    fileToCheck = open("testfiles/" + inputFilename, 'r')
    checkLine = ""
    while(checkLine[0:2] != "ET"):
        checkLine = fileToCheck.readline()
    fileToCheck.close()
    if("LINK180" in checkLine):
        print("\n***********************************************")
        print("File loaded successfully! Element type: LINK180")
        print("***********************************************\n")
        return "LINK180"
    else:
        print("Error! Element type incorrect or not found!")

def getCharPosition(givenString, char):
    position = []
    for n in range(len(givenString)):
        if givenString[n] == char:
            position.append(n)
    return position