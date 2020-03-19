from fileOperations import loadInputFile, checkElementType
from preprocessor.preprocessorTruss import runPreprocessorModule

if __name__ == "__main__":
    inputFilename = loadInputFile()
    elementType = checkElementType(inputFilename)
    # PREPROCESSOR #
    runPreprocessorModule(inputFilename, elementType)