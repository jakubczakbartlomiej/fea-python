from fileOperations import loadInputFile, checkInputFile
from preprocessor.preprocessorTruss import runPreprocessorModule

if __name__ == "__main__":
    # PREPROCESSOR #
    inputFilename = loadInputFile()
    elementType, amount = checkInputFile(inputFilename)
    runPreprocessorModule(inputFilename, elementType, amount)
    ################