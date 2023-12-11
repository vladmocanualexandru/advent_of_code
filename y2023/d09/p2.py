import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 971
 
def getInputData(inputFile):
    raw = getTuples_numbers(inputFile)
    
    processed=[entry for entry in raw]

    return processed 

def calculateLastValue(numbers):
    newNumbers = []
    
    allZeroes = numbers[0] == 0
    for numberId in range(1, len(numbers), 1):
        newNumbers.append(numbers[numberId] - numbers[numberId-1])
        if numbers[numberId]!=0:
            allZeroes = False

    # log(newNumbers)
    if not allZeroes:
        lastValue = calculateLastValue(newNumbers)
        return newNumbers[0]-lastValue
    else:
        return 0


def solution(inputFile):
    result = 0
    
    numbersArr = getInputData(inputFile)

    for numbers in numbersArr:
        result += numbers[0] - calculateLastValue(numbers)
        

    # log(red())
    return (result, EXPECTED_RESULT)