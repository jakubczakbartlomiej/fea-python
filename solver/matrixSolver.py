import numpy as np 

def calculateDisplacements(loadVector, stiffnessMatrix):
    print(stiffnessMatrix)
    print("")
    print(loadVector)
    print("")
    nodalDisplacements = np.dot(loadVector, stiffnessMatrix)
    return nodalDisplacements