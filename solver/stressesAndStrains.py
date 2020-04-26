import numpy as np 

def findStressAndStrain(nodalCoordinates, nodalDisplacements, materials, nodesOfElement, numberOfNodesInElement, entitiesAmount):
    numberOfElements = entitiesAmount[2]
    elementStress = np.zeros(entitiesAmount[2])
    elementStrain = np.zeros(entitiesAmount[2])
    elementForce  = np.zeros(entitiesAmount[2])
    elementNodalCoordinates = np.zeros(4)
    elementNodalDisplacement = np.zeros(4)
    elementDegreeOfFreedom = np.zeros(2 * numberOfNodesInElement)
    for i in range(0, numberOfElements):
        for j in range(0, numberOfNodesInElement):
            elementNodalCoordinates[(2*j-1)+1] = nodalCoordinates[int(nodesOfElement[i,j])-1,0]
            elementNodalCoordinates[(2*j)+1] = nodalCoordinates[int(nodesOfElement[i,j])-1,1]
            elementDegreeOfFreedom[(2*j-1)+1] = 2 * int(nodesOfElement[i,j]) - 1
            elementDegreeOfFreedom[(2*j)+1] = 2 * int(nodesOfElement[i,j])
            elementNodalDisplacement[(2*j-1)+1] = nodalDisplacements[int(elementDegreeOfFreedom[(2*j-1)+1])-1]
            elementNodalDisplacement[(2*j)+1] = nodalDisplacements[int(elementDegreeOfFreedom[(2*j)+1])-1]
  
        youngModulus = materials[int(nodesOfElement[i,2])-1,0]
        elementArea = materials[int(nodesOfElement[i,2])-1,2] 
        deltaX = float(elementNodalCoordinates[2]) - float(elementNodalCoordinates[0])
        deltaY = float(elementNodalCoordinates[3]) - float(elementNodalCoordinates[1])
        L = (deltaX * deltaX + deltaY * deltaY)**(1/2)
        deltaU = float(elementNodalDisplacement[2]) - float(elementNodalDisplacement[0])
        deltaV = float(elementNodalDisplacement[3]) - float(elementNodalDisplacement[1])

        elementStrain[i] = (deltaU * deltaX + deltaV * deltaY)/L**2
        elementStress[i] = youngModulus * elementStrain[i]
        elementForce[i]  = elementStrain[i] * youngModulus * elementArea

    return elementStress, elementStrain, elementForce   