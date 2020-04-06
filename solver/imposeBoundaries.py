import numpy as np

def imposeBoundaryConditions(amount, loads, loadVector, stiffnessMatrix):
    numberOfSupports = amount[3]
    for i in range(0,numberOfSupports):
        degreeOfFreedom = 2*int(loads[i,0])-2 + int(loads[i,1])
        print(degreeOfFreedom)
    return loadVector, stiffnessMatrix