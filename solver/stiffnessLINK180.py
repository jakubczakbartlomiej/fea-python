import numpy as np

def calculateElementStiffnessMatrix(youngModulus, elementArea, elementNodalCoordinates):
    elementStiffnessMatrix = np.zeros(shape=(4,4))
    deltaX = float(elementNodalCoordinates[2]) - float(elementNodalCoordinates[0])
    deltaY = float(elementNodalCoordinates[3]) - float(elementNodalCoordinates[1])
    L = (deltaX * deltaX + deltaY * deltaY)**(1/2)
    coefficient = youngModulus * elementArea/L**3
    
    elementStiffnessMatrix[0,0] = coefficient * deltaX * deltaX
    elementStiffnessMatrix[0,1] = coefficient * deltaX * deltaY
    elementStiffnessMatrix[0,2] = -coefficient * deltaX * deltaX
    elementStiffnessMatrix[0,3] = -coefficient * deltaX * deltaY
    elementStiffnessMatrix[1,0] = coefficient * deltaX * deltaY
    elementStiffnessMatrix[1,1] = coefficient * deltaY * deltaY
    elementStiffnessMatrix[1,2] = -coefficient * deltaX * deltaY
    elementStiffnessMatrix[1,3] = -coefficient * deltaY * deltaY
    elementStiffnessMatrix[2,0] = -coefficient * deltaX * deltaX
    elementStiffnessMatrix[2,1] = -coefficient * deltaX * deltaY
    elementStiffnessMatrix[2,2] = coefficient * deltaX * deltaX
    elementStiffnessMatrix[2,3] = coefficient * deltaX * deltaY
    elementStiffnessMatrix[3,0] = -coefficient * deltaX * deltaY
    elementStiffnessMatrix[3,1] = -coefficient * deltaY * deltaY
    elementStiffnessMatrix[3,2] = coefficient * deltaX * deltaY
    elementStiffnessMatrix[3,3] = coefficient * deltaY * deltaY
    return elementStiffnessMatrix

def buildStiffnessMatrix(amount, materials, nodalCoordinates, nodesOfElement):
    numberOfNodes = amount[1]
    numberOfElements = amount[2]
    numberOfNodesInElement = 2
    elementNodalCoordinates = np.zeros(4)
    elementDegreeOfFreedom = np.zeros(2 * numberOfNodesInElement)
    stiffnessMatrix = np.zeros(shape = (2 * numberOfNodes ,2 * numberOfNodes))
    for i in range(0, numberOfElements):
        for j in range(0, numberOfNodesInElement):
            elementNodalCoordinates[(2*j-1)+1] = nodalCoordinates[int(nodesOfElement[i,j])-1,0]
            elementNodalCoordinates[(2*j)+1] = nodalCoordinates[int(nodesOfElement[i,j])-1,1]
            elementDegreeOfFreedom[(2*j-1)+1] = 2 * int(nodesOfElement[i,j]) - 1
            elementDegreeOfFreedom[(2*j)+1] = 2 * int(nodesOfElement[i,j])
        youngModulus = materials[int(nodesOfElement[i,2])-1,0] 
        elementArea = materials[int(nodesOfElement[i,2])-1,2]
        elementStiffnessMatrix = calculateElementStiffnessMatrix(youngModulus, elementArea, elementNodalCoordinates)
        for row in range(0, 2 * numberOfNodesInElement - 1):
            for column in range(0, 2 * numberOfNodesInElement - 1):
                stiffnessMatrix[int(elementDegreeOfFreedom[row]), int(elementDegreeOfFreedom[column])] = \
                    stiffnessMatrix[int(elementDegreeOfFreedom[row]), int(elementDegreeOfFreedom[column])] + float(elementStiffnessMatrix[row,column])
    return stiffnessMatrix