from preprocessor.fileOperations import loadInputFile, checkInputFile
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
    elementType, entitiesAmount = checkInputFile(inputFilename)
    nodalCoordinates, materials, elements, loads, supports, nodesOfElement, numberOfNodesInElement = runPreprocessorModule(inputFilename, elementType, entitiesAmount)
    ################

    # SOLVER # 
    loadVector, numberOfNodes = buildLoadVector(nodalCoordinates, loads)
    stiffnessMatrix = buildStiffnessMatrix(nodalCoordinates, materials, nodesOfElement, numberOfNodesInElement, entitiesAmount)
    loadVectorImposed, stiffnessMatrixImposed = imposeBoundaryConditions(loadVector, supports, stiffnessMatrix, entitiesAmount)
    nodalDisplacements, compliance, calculationTime = calculateDisplacements(loadVectorImposed, stiffnessMatrixImposed)
    elementStress, elementStrain, elementForce = findStressAndStrain(nodalCoordinates, nodalDisplacements, \
        materials, nodesOfElement, numberOfNodesInElement, entitiesAmount)
    ##########

    # POSTPROCESSOR #
    writeResultsToFile(inputFilename, elementType, nodalCoordinates, nodalDisplacements, materials, elements, \
        supports, loadVectorImposed, entitiesAmount, elementStrain, elementStress, elementForce, compliance, calculationTime)