from datetime import datetime

def writeResultsToFile(inputFilename, elementType, nodalCoordinates, nodalDisplacements, materials, elements, \
        supports, loadVectorImposed, entitiesAmount, elementStrain, elementStress, elementForce, compliance, calculationTime):
    numberOfNodes = entitiesAmount[1]
    numberOfElements = entitiesAmount[2]
    numberOfSupports = entitiesAmount[3]
    now = datetime.now()
    if ".txt" in inputFilename:
        inputFilename = inputFilename[:-4]
    outputFile = open("resultFiles/" + inputFilename +"-RESULTS.txt", 'w')
    outputFile.write("Simulation performed at: " + now.strftime("%d/%m/%Y %H:%M:%S") + "\n\n")
    outputFile.write("ELEMENT TYPE: " + elementType + "\n")
    outputFile.write("NUMBER OF APPLIED MATERIALS: " + str(entitiesAmount[0]) + "\n")
    outputFile.write("NUMBER OF NODES: " + str(entitiesAmount[1]) + "\n")
    outputFile.write("NUMBER OF ELEMENTS: " + str(entitiesAmount[2]) + "\n")
    outputFile.write("NUMBER OF SUPPORTS: " + str(entitiesAmount[3]) + "\n")
    outputFile.write("NUMBER OF LOADS: " + str(entitiesAmount[4]) + "\n")
    outputFile.write("COMPLIANCE: " + str(compliance) + "\n")
    outputFile.write("CALCULATION TIME: " + str(calculationTime) + " seconds\n")
    outputFile.write("\n\n******************* NODAL DISPLACEMENTS ***********************\n")
    outputFile.write("\n[NODE_ID]          [UX]              [UY]              [FX]              [FY]\n")
    for i in range(0,numberOfNodes):
        outputFile.write("    " + str(i+1) + \
            "          " + str("%.9f" % nodalDisplacements[2*i])[:11] + \
                "       " + str("%.9f" % nodalDisplacements[2*i+1])[:11] + \
                    "       " + str("%.9f" % loadVectorImposed[2*i])[:11] + \
                        "       " + str("%.9f" % loadVectorImposed[2*i+1])[:11] + "\n")
    outputFile.write("\n\n**************** ELEMENT STRESS AND STRAIN ********************\n")
    outputFile.write("\n[ELEMENT_ID]          [ELEMENT_STRAIN]              [ELEMENT_STRESS]              [ELEMENT_FORCE]\n")
    for i in range(0,numberOfElements):
        outputFile.write("     " + str(i+1) + "                  " + str("%.9f" % elementStrain[i])[:11] + \
            "                   " + str("%.9f" % elementStress[i])[:11] + \
                "                   " + str("%.9f" % elementForce[i])[:11] + "\n")
    outputFile.write("\n\n***************** ELEMENTS AND PROPERTIES *********************\n")
    outputFile.write("\n[ELEMENT_ID]          [EX]             [AREA]          [ELEMENT_NODE1]          [ELEMENT_NODE2]\n")
    for i in range(0,numberOfElements):
        outputFile.write("     " + str(i+1) + "             " + str("%.9f" % materials[int(elements[i,2])-1,0])[:11] + \
             "      " + str("%.9f" % materials[int(elements[i,2])-1,2])[:11] + \
                 "               " + str(int(elements[i,0])) + \
                     "                        " + str(int(elements[i,1])) + "\n")
    outputFile.write("\n\n************************ SUPPORTS *****************************\n")
    outputFile.write("\n[SUPPORT_TYPE]          [NODE_ID]          [DIRECTION]          [VALUE]\n")
    for i in range(0,numberOfSupports):
        outputFile.write("       " + str(supports[i,0]) + "                    " + str(supports[i,1]) + \
            "                  " + str(supports[i,2]) + "                 " + str(supports[i,3]) + "\n")
    outputFile.write("\n\n******************** NODAL COORDINATES ************************\n")
    outputFile.write("\n[NODE_ID]          [X-COORDINATE]          [Y-COORDINATE]\n")
    for i in range(0,numberOfNodes):
        outputFile.write("    " + str(i+1) + "                   " + str("%.3f" % nodalCoordinates[i,0])[:5] + \
            "                  " + str("%.3f" % nodalCoordinates[i,1])[:5] + "\n")
    outputFile.write("\nFINISH")
    outputFile.close()
    print("\nFINISHED! RESULTS ARE STORED IN: resultFiles/" + inputFilename + "-RESULTS.txt")
    print("\nCLOSING...")