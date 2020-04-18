from fileOperations import loadInputFile, checkInputFile
from preprocessor.gatherDataFromFile import runPreprocessorModule
from solver.buildLoadVector import buildLoadVector
from solver.stiffnessLINK180 import buildStiffnessMatrix
from solver.imposeBoundaries import imposeBoundaryConditions
from solver.stressesAndStrains import findStressAndStrain
from solver.matrixSolver import calculateDisplacements
from postprocessor.saveResults import writeResultsToFile

if __name__ == "__main__":
    # PREPROCESSOR #
    inputFilename = loadInputFile()
    elementType, amount = checkInputFile(inputFilename)
    nodalCoordinates, loads, supports, nodesOfElement, materials, elements, numberOfNodesInElement = runPreprocessorModule(inputFilename, elementType, amount)
    ################

    # SOLVER # 
    numberOfNodes, loadVector = buildLoadVector(nodalCoordinates, loads)
    stiffnessMatrix = buildStiffnessMatrix(amount, materials, nodalCoordinates, nodesOfElement, numberOfNodesInElement)
    loadVectorImposed, stiffnessMatrixImposed = imposeBoundaryConditions(amount, supports, loadVector, stiffnessMatrix)
    nodalDisplacement, compliance, calculationTime = calculateDisplacements(loadVectorImposed, stiffnessMatrixImposed)
    elementStess, elementStrain, elementForce = findStressAndStrain(amount, nodalDisplacement, nodalCoordinates, \
        nodesOfElement, numberOfNodesInElement, materials)
    ##########

    # POSTPROCESSOR #
    writeResultsToFile(inputFilename, elementType, nodalDisplacement, loadVectorImposed, compliance, \
        calculationTime, amount, materials, elements, supports, nodalCoordinates, elementStrain, elementStess, elementForce)