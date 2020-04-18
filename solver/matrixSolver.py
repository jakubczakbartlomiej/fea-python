import numpy as np 
import time

def calculateDisplacements(loadVector, stiffnessMatrix):
    print("\nSTARTING CALCULATIONS...")
    startTime = time.time()
    nodalDisplacements = np.matmul(loadVector,np.linalg.inv(stiffnessMatrix))
    print("CALCULATIONS ARE COMPLETED!")
    compliance = np.matmul(loadVector, nodalDisplacements)
    calculationTime = "%.9f" % (time.time() - startTime)
    print("******************************************")
    print("COMPLIANCE: " + str(compliance))
    print("CALCULATIONS HAS BEEN DONE IN: " + str(calculationTime) + " SECONDS ")
    print("******************************************")
    print("\nPROCESSING TO POSTPROCESSOR MODULE...")
    return nodalDisplacements, compliance, calculationTime