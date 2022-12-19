import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 99145

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    compressedString = getInputData(inputFile)

    result = 0

    startIndex = 0
    while startIndex<len(compressedString):
        if compressedString[startIndex] == '(':
            for stopIndex in range(startIndex+1, len(compressedString)):
                if compressedString[stopIndex] == ')':
                    markerData = compressedString[startIndex+1:stopIndex].split('x')
                    # log('marker', markerData)
                    startIndex = stopIndex+1+int(markerData[0])
                    result += int(markerData[0])*int(markerData[1])
                    break
        else:
            startIndex+=1
            result+=1

    return (result,EXPECTED_RESULT)

 

