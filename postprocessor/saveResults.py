from datetime import datetime

def writeResultsToFile(inputFilename, elementType, nodalDisplacements, loadVector, compliance, calculationTime, amount):
    now = datetime.now()
    if ".txt" in inputFilename:
        inputFilename = inputFilename[:-4]
    outputFile = open("resultFiles/" + inputFilename +"-RESULTS.txt", 'w')
    outputFile.write("Simulation performed at: " + now.strftime("%d/%m/%Y %H:%M:%S") + "\n\n")
    outputFile.write("ELEMENT TYPE: " + elementType + "\n")
    outputFile.write("NUMBER OF APPLIED MATERIALS: " + str(amount[0]) + "\n")
    outputFile.write("NUMBER OF NODES: " + str(amount[1]) + "\n")
    outputFile.write("NUMBER OF ELEMENTS: " + str(amount[2]) + "\n")
    outputFile.write("NUMBER OF SUPPORTS: " + str(amount[3]) + "\n")
    outputFile.write("NUMBER OF LOADS: " + str(amount[4]) + "\n")
    outputFile.write("COMPLIANCE: " + str(compliance) + "\n")
    outputFile.write("CALCULATION TIME: " + str(calculationTime) + " s\n")
    outputFile.write("\n\n******************* NODAL DISPLACEMENTS ***********************\n")
    outputFile.write("\n[NODE_ID]          [DX]              [DY]              [FX]              [FY]\n")
    for i in range(0,amount[1]):
        outputFile.write("    " + str(i+1) + \
            "          " + str("%.9f" % nodalDisplacements[2*i])[:11] + \
                "       " + str("%.9f" % nodalDisplacements[2*i+1])[:11] + \
                    "       " + str("%.9f" % loadVector[2*i])[:11] + \
                        "       " + str("%.9f" % loadVector[2*i+1])[:11] + "\n")
    outputFile.write("\n\n***************** ELEMENTS AND PROPERTIES *********************\n")
    outputFile.write("\n[ELEMENT_ID]          [EX]          [AREA]          [ELEMENT_NODE1]          [ELEMENT_NODE2]\n")
    for i in range(0,amount[2]):
        outputFile.write("     " + str(i+1) + "\n")

    outputFile.write("\n\n************************ SUPPORTS *****************************\n")
    outputFile.write("\n[SUPPORT_TYPE]          [NODE_ID]          [DIRECTION]          [VALUE]\n")

    outputFile.write("\n\n******************** NODAL COORDINATES *********  ***************\n")
    outputFile.write("\n[NODE_ID]          [X-COORDINATE]          [Y-COORDINATE]\n")