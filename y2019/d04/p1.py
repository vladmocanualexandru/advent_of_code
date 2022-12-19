import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 2081

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'-')
    
    processed=raw[0]

    return processed 

def checkConditions(candidate):
    candidateStr = str(candidate)

    doubleCharFound = False
    for i in range(len(candidateStr)-1):
        if candidateStr[i]==candidateStr[i+1]:
            doubleCharFound = True

        if candidateStr[i]>candidateStr[i+1]:
            return False

    return doubleCharFound


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])


    result = sum([1 for candidate in range(inputData[0], inputData[1]+1) if checkConditions(candidate)])

    return (result,EXPECTED_RESULT)

 
