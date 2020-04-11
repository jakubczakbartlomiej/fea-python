from fileOperations import loadInputFile, checkInputFile
from preprocessor.gatherDataFromFile import runPreprocessorModule
from solver.buildLoadVector import buildLoadVector
from solver.stiffnessLINK180 import buildStiffnessMatrix
from solver.imposeBoundaries import imposeBoundaryConditions
from solver.matrixSolver import calculateDisplacements

if __name__ == "__main__":
    # PREPROCESSOR #
    inputFilename = loadInputFile()
    elementType, amount = checkInputFile(inputFilename)
    nodalCoordinates, loads, supports, nodesOfElement, materials = runPreprocessorModule(inputFilename, elementType, amount)
    ################

    # SOLVER # 
    numberOfNodes, loadVector = buildLoadVector(nodalCoordinates, loads)
    stiffnessMatrix = buildStiffnessMatrix(amount, materials,nodalCoordinates, nodesOfElement)
    loadVector, stiffnessMatrix = imposeBoundaryConditions(amount, supports, loadVector, stiffnessMatrix)
    nodalDisplacement = calculateDisplacements(loadVector, stiffnessMatrix)
    print(nodalDisplacement)
    ##########