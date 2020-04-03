from fileOperations import loadInputFile, checkInputFile
from preprocessor.gatherDataFromFile import runPreprocessorModule
from solver.buildLoadVector import buildLoadVector
from solver.stiffnessLINK180 import buildStiffnessMatrix

if __name__ == "__main__":
    # PREPROCESSOR #
    inputFilename = loadInputFile()
    elementType, amount = checkInputFile(inputFilename)
    nodalCoordinates, loads, nodesOfElement, materials = runPreprocessorModule(inputFilename, elementType, amount)
    ################

    # SOLVER # 
    numberOfNodes, loadVector = buildLoadVector(nodalCoordinates, loads)
    buildStiffnessMatrix(amount, materials,nodalCoordinates, nodesOfElement)
    ##########