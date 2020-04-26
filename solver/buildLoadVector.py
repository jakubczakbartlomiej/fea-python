import numpy as np

def buildLoadVector(nodalCoordinates, loads):
    print("\nBUILDING LOAD VECTOR...")
    numberOfLoads = np.size(loads,0)
    numberOfNodes = 2 * np.size(nodalCoordinates,0)
    loadVector = np.zeros(numberOfNodes)
    for i in range(0,numberOfLoads):
        if loads[i,2] == "X":
            loadVector[2*loads[i,1]-2] = loads[i,3]
        elif loads[i,2] == "Y":
            loadVector[2*loads[i,1]-1] = loads[i,3]
    print("COMPLETED! SIZE OF THE LOAD VECTOR: " + str(numberOfNodes) + "\n")
    return loadVector, numberOfNodes