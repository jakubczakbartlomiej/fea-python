import numpy as np

def imposeBoundaryConditions(amount, supports, loadVector, stiffnessMatrix):
    numberOfSupports = amount[3]
    #print(loadVector)
    #print("")
    for i in range(0,numberOfSupports):
        if supports[i,2] == "UX":
            degreeOfFreedom = 2 * int(supports[i,1]) - 2 + 1
        elif supports[i,2] == "UY":
            degreeOfFreedom = 2 * int(supports[i,1]) - 2 + 2
        #print(degreeOfFreedom)
        loadVector[degreeOfFreedom-1] = float(supports[i,3])
        stiffnessMatrix[:,degreeOfFreedom] = 0
        stiffnessMatrix[degreeOfFreedom,:] = 0
        stiffnessMatrix[degreeOfFreedom,degreeOfFreedom] = 1
    return loadVector, stiffnessMatrix