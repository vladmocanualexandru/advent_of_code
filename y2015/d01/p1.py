import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 74

def getInputData(inputFile):
    raw = getRawText(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    floor = 0

    for i in range(len(inputData)):
        c = inputData[i]

        if c == '(':
            floor+=1
        else:
            floor-=1

    result = floor
    return (result, EXPECTED_RESULT)

 