from fileOperations import loadInputFile, checkInputFile
from preprocessor.gatherDataFromFile import runPreprocessorModule
from solver.buildVectors import buildLoadVector

if __name__ == "__main__":
    # PREPROCESSOR #
    inputFilename = loadInputFile()
    elementType, amount = checkInputFile(inputFilename)
    nodalCoordinates, loads = runPreprocessorModule(inputFilename, elementType, amount)
    ################

    # SOLVER # 
    loadVector = buildLoadVector(nodalCoordinates, loads)
    ##########