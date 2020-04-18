import numpy as np
import sys

def showStatistics(elementType, amount):
    print("\n")
    print("******************************************")
    print("THE PREPROCESSOR MODULE HAS EXECUTED SUCCESSFULLY!")
    print("STATISTICS: ")
    print("ELEMENT TYPE: " + elementType)
    print("NUMBER OF APPLIED MATERIALS: " + str(amount[0]))
    print("NUMBER OF NODES: " + str(amount[1]))
    print("NUMBER OF ELEMENTS: " + str(amount[2]))
    print("NUMBER OF SUPPORTS: " + str(amount[3]))
    print("NUMBER OF LOADS: " + str(amount[4]))
    print("******************************************")
    print("\n")
    print("PROCESSING TO SOLVER MODULE...")


def runPreprocessorModule(inputFilename, elementType, amount):
    
    # GLOBAL VARIABLES #
    materials = np.zeros(shape=(amount[0],3))
    nodalCoordinates = np.zeros(shape=(amount[1],2))
    elements = np.zeros(shape=(amount[2],3))
    nodesOfElement = np.zeros(shape=(amount[2],3))
    supports = np.zeros(shape=(amount[3],4), dtype=object)
    loads = np.zeros(shape=(amount[4],4), dtype=object)

    supportsCounter = 0
    loadsCounter = 0
    ####################

    checkLine = ""
    if(elementType == "LINK180"): 
        inputFile = open("inputFiles/" + inputFilename, 'r')
        while(checkLine != "FINISH"):
            checkLine = inputFile.readline()
            if("MAT," in checkLine[:4]):
                gatheredProperties = checkLine.rsplit(", ")
                materials[int(gatheredProperties[1])-1,0] = float(gatheredProperties[2])
                materials[int(gatheredProperties[1])-1,1] = float(gatheredProperties[3])
                materials[int(gatheredProperties[1])-1,2] = float(gatheredProperties[4])
            if("N," in checkLine[:2]):
                gatheredProperties = checkLine.rsplit(", ")
                nodalCoordinates[int(gatheredProperties[1])-1,0] = float(gatheredProperties[2])
                nodalCoordinates[int(gatheredProperties[1])-1,1] = float(gatheredProperties[3])
            if("EN," in checkLine[:3]):
                gatheredProperties = checkLine.rsplit(", ")
                elements[int(gatheredProperties[1])-1,0] = int(gatheredProperties[3])
                elements[int(gatheredProperties[1])-1,1] = int(gatheredProperties[4])
                elements[int(gatheredProperties[1])-1,2] = int(gatheredProperties[2])
                nodesOfElement[int(gatheredProperties[1])-1,2] = int(gatheredProperties[2])
                nodesOfElement[int(gatheredProperties[1])-1,0] = int(gatheredProperties[3])
                nodesOfElement[int(gatheredProperties[1])-1,1] = int(gatheredProperties[4])
            if("D," in checkLine[:2]):
                supportsCounter += 1
                gatheredProperties = checkLine.rsplit(", ")
                supports[supportsCounter-1,0] = str(gatheredProperties[0])
                supports[supportsCounter-1,1] = int(gatheredProperties[1])
                supports[supportsCounter-1,2] = str(gatheredProperties[2])
                supports[supportsCounter-1,3] = float(gatheredProperties[3])
            if("F," in checkLine[:2]):
                loadsCounter += 1
                gatheredProperties = checkLine.rsplit(", ")
                loads[loadsCounter-1,0] = str(gatheredProperties[0])
                loads[loadsCounter-1,1] = int(gatheredProperties[1])
                loads[loadsCounter-1,2] = str(gatheredProperties[2])
                loads[loadsCounter-1,3] = float(gatheredProperties[3])
        showStatistics(elementType, amount)
        return nodalCoordinates, loads, supports, nodesOfElement, materials
                
