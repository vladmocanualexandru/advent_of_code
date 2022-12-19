import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 1766397

WEAKNESS_TARGET_SCORE = 14144619

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):

    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result=None


    startIndex = 0
    stopIndex = 1

    while startIndex<stopIndex and stopIndex<len(inputData):
        currentScore = sum(inputData[startIndex:stopIndex+1])

        if currentScore == WEAKNESS_TARGET_SCORE:
            result = min(inputData[startIndex:stopIndex+1]) + max(inputData[startIndex:stopIndex+1])
            break

        if currentScore<WEAKNESS_TARGET_SCORE:
            stopIndex+=1
        else:
            startIndex+=1

    return (result, EXPECTED_RESULT)

 
