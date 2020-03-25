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
    print("NUMBER OF LOADS: " + str(amount[3]))
    print("******************************************")
    print("\n")
    print("PROCESSING TO SOLVER MODULE...")


def runPreprocessorModule(inputFilename, elementType, amount):
    
    # GLOBAL VARIABLES #
    materials = np.empty(shape=(amount[0],2))
    nodalCoordinates = np.empty(shape=(amount[1],2))
    elements = np.empty(shape=(amount[2],3))
    loads = np.empty(shape=(amount[3],4), dtype=object)
    ####################

    checkLine = ""
    if(elementType == "LINK180"): 
        inputFile = open("testfiles/" + inputFilename, 'r')
        while(checkLine != "FINISH"):
            checkLine = inputFile.readline()
            if("MAT," in checkLine[:4]):
                gatheredProperties = checkLine.rsplit(", ")
                materials[int(gatheredProperties[1])-1,0] = float(gatheredProperties[2])
                materials[int(gatheredProperties[1])-1,1] = float(gatheredProperties[3])
            if("N," in checkLine[:2]):
                gatheredProperties = checkLine.rsplit(", ")
                nodalCoordinates[int(gatheredProperties[1])-1,0] = float(gatheredProperties[2])
                nodalCoordinates[int(gatheredProperties[1])-1,1] = float(gatheredProperties[3])
            if("EN," in checkLine[:3]):
                gatheredProperties = checkLine.rsplit(", ")
                elements[int(gatheredProperties[1])-1,0] = int(gatheredProperties[3])
                elements[int(gatheredProperties[1])-1,1] = int(gatheredProperties[4])
                elements[int(gatheredProperties[1])-1,2] = int(gatheredProperties[2])
            if("F," in checkLine[:2]):
                gatheredProperties = checkLine.rsplit(", ")
                loads[int(gatheredProperties[1])-1,0] = str(gatheredProperties[0])
                loads[int(gatheredProperties[1])-1,1] = int(gatheredProperties[2])
                loads[int(gatheredProperties[1])-1,2] = str(gatheredProperties[3])
                loads[int(gatheredProperties[1])-1,3] = float(gatheredProperties[4])
        showStatistics(elementType, amount)
                
