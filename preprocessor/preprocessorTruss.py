import numpy as np
from fileOperations import getCharPosition

def runPreprocessorModule(inputFilename, elementType):
    checkLine = ""
    if(elementType == "LINK180"): 
        inputFile = open("testfiles/" + inputFilename, 'r')
        while(checkLine[0:1] != "P"):
            checkLine = inputFile.readline()
            if("EX" in checkLine):
                gatheredProperties = checkLine.rplit(",")
                print(gatheredProperties)
