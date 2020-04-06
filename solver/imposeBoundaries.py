import numpy as np

def imposeBoundaryConditions(amount, supports, loadVector, stiffnessMatrix):
    numberOfSupports = amount[3]
    for i in range(0,numberOfSupports):
        degreeOfFreedom = 2*int(supports[i,1])-2 + int(supports[i,2])
        print(degreeOfFreedom)
    return loadVector, stiffnessMatrix