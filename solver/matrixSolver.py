import numpy as np 
import time

def calculateDisplacements(loadVector, stiffnessMatrix):
    startTime = time.time()
    nodalDisplacements = np.matmul(loadVector,np.linalg.inv(stiffnessMatrix))
    print("\nCALCULATIONS ARE COMPLETED!")
    compliance = np.matmul(loadVector, nodalDisplacements)
    calculationTime = "%.9f" % (time.time() - startTime)
    print("******************************************")
    print("COMPLIANCE: " + str(compliance))
    print("CALCULATIONS HAS BEEN DONE IN: " + str(calculationTime) + " SECONDS ")
    print("******************************************")
    return nodalDisplacements, compliance, calculationTime