import os
import sys
import numpy as np

def loadInputFile():
    os.system('cls')
    testFilesList = os.listdir("testfiles")
    i = 1
    for specificFile in testFilesList:
        print(str(i) + ".  " + str(specificFile))
        i += 1
    userChoice = input("Which file would you like to use? (insert number and press ENTER): ")
    return testFilesList[int(userChoice)-1]

def checkInputFile(inputFilename):
    fileToCheck = open("testfiles/" + inputFilename, 'r')
    print("\n\nOpening "+ inputFilename + "...")
    checkLine = ""
    elementType = ""
    amount = [0, 0, 0, 0] # amount of [MAT, N, EN, F]
    while(checkLine != ["FINISH"]):
        checkLine = fileToCheck.readline()
        if("LINK180" in checkLine):
            elementType = "LINK180"
        checkLine = checkLine.rsplit(", ")
        if("MAT" in checkLine):
            amount[0] += 1
        if("N" in checkLine):
            amount[1] += 1
        if("EN" in checkLine):
            amount[2] += 1
        if("F" in checkLine):
            amount[3] += 1
        
    fileToCheck.close()
    if(elementType == ""):
        print("\n*******************************")
        print("ERROR! NO ELEMENT TYPE DEFINED!")
        print("*********************************\n")
        sys.exit("PREPROCESSOR ERROR")
    if(amount[0] == 0):
        print("\n*******************************")
        print("ERROR! MATERIALS ARE NOT DEFINED!")
        print("*********************************\n")
        sys.exit("PREPROCESSOR ERROR")
    if(amount[1] == 0):
        print("\n***************************")
        print("ERROR! NODES ARE NOT FOUND!")
        print("*****************************\n")
        sys.exit("PREPROCESSOR ERROR")
    if(amount[2] == 0):
        print("\n***************************")
        print("ERROR! ELEMENTS ARE NOT FOUND!")
        print("*****************************\n")
        sys.exit("PREPROCESSOR ERROR")
    if(amount[3] == 0):
        print("\n***************************")
        print("ERROR! LOADS ARE NOT FOUND!")
        print("*****************************\n")
        sys.exit("PREPROCESSOR ERROR")
    return elementType, amount