import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 3737498

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'x')
    
    processed=raw

    return processed 

def calculateRibbonLength(numberTuple):
    numberTuple.sort()
    return 2*numberTuple[0]+2*numberTuple[1] + numberTuple[0]*numberTuple[1]*numberTuple[2]

def solution(inputFile):
    inputData = getInputData(inputFile)

    result = 0

    for tuple in inputData:
        result += calculateRibbonLength(tuple)

    return (result, EXPECTED_RESULT)

 