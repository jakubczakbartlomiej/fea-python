import numpy as np 

def calculateDisplacements(loadVector, stiffnessMatrix):
    nodalDisplacements = np.dot(loadVector, stiffnessMatrix)
    return nodalDisplacements