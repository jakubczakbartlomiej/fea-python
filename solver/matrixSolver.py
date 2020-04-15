import numpy as np 

def calculateDisplacements(loadVector, stiffnessMatrix):
    nodalDisplacements = np.matmul(loadVector,np.linalg.inv(stiffnessMatrix))
    print("\nCALCULATIONS ARE COMPLETED!")
    compliance = np.matmul(loadVector, nodalDisplacements)
    print("******************************************")
    print("COMPLIANCE: " + str(compliance))
    print("******************************************")
    return nodalDisplacements