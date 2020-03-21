import numpy as np
from fileOperations import youngX, poissonXY


def runPreprocessorModule(inputFilename, elementType):
    checkLine = ""
    if(elementType == "LINK180"): 
        inputFile = open("testfiles/" + inputFilename, 'r')
        while(checkLine != "FINISH"):
            checkLine = inputFile.readline()
            if("EX" in checkLine):
                gatheredProperties = checkLine.rsplit(",")
                youngX.insert(int(gatheredProperties[2]),float(gatheredProperties[3]))
            if("PRXY" in checkLine):
                gatheredProperties = checkLine.rsplit(",")
                poissonXY.insert(int(gatheredProperties[2]),float(gatheredProperties[3]))
                
