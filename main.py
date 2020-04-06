from fileOperations import loadInputFile, checkInputFile
from preprocessor.gatherDataFromFile import runPreprocessorModule
from solver.buildLoadVector import buildLoadVector
from solver.stiffnessLINK180 import buildStiffnessMatrix
from solver.imposeBoundaries import imposeBoundaryConditions

if __name__ == "__main__":
    # PREPROCESSOR #
    inputFilename = loadInputFile()
    elementType, amount = checkInputFile(inputFilename)
    nodalCoordinates, loads, nodesOfElement, materials = runPreprocessorModule(inputFilename, elementType, amount)
    ################

    # SOLVER # 
    numberOfNodes, loadVector = buildLoadVector(nodalCoordinates, loads)
    stiffnessMatrix = buildStiffnessMatrix(amount, materials,nodalCoordinates, nodesOfElement)
    loadVector, stiffnessMatrix = imposeBoundaryConditions(amount, loads, loadVector, stiffnessMatrix)
    ##########