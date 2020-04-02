import numpy as np

def buildStiffnessMatrix(amount, nodalCoordinates, nodesOfElement):
    numberOfNodes = amount[1]
    numberOfElements = amount[2]
    numberOfNodesInElement = 2
    elementNodalCoordinates = np.zeros(4)
    elementDegreeOfFreedom = np.zeros(2 * numberOfNodes)
    stiffnessMatrix = np.zeros(shape = (2 * numberOfNodes ,2 * numberOfNodes))
    for i in range(1,numberOfElements):
        for j in range(1, numberOfNodesInElement):
            elementNodalCoordinates[2*j-1] = nodalCoordinates[int(nodesOfElement[i,j]),1]
            elementNodalCoordinates[2*j] = nodalCoordinates[int(nodesOfElement[i,j]),2]
            elementDegreeOfFreedom[2*j-1] = 2 * int(nodesOfElement[i,j]) - 1
            elementDegreeOfFreedom[2*j] = 2 * int(nodesOfElement[i,j])
    

