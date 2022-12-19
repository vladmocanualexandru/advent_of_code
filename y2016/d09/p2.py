from bz2 import compress
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 10943094568

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw[0]

    return processed

def calculateLength(string, multiplier):

    result = 0
    startIndex = 0
    while startIndex<len(string):
        if string[startIndex] == '(':
            for stopIndex in range(startIndex+1, len(string)):
                if string[stopIndex] == ')':
                    markerData = string[startIndex+1:stopIndex].split('x')
                    
                    result += calculateLength(string[stopIndex+1:stopIndex+1+int(markerData[0])], int(markerData[1]))
                    
                    startIndex = stopIndex+1+int(markerData[0])
                    break
        else:
            startIndex+=1
            result+=1

    return result * multiplier 


def solution(inputFile):
    compressedString = getInputData(inputFile)

    result = calculateLength(compressedString, 1)

    return (result,EXPECTED_RESULT)

 

