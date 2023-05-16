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

EXPECTED_RESULT = None
 
def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)

    return raw[0] 

def calculateDivSum(number):
    result = 1 + number
    for div in range(2, int(number/2)+1, 1):
         if number % div == 0:
             result += div

    return result


def solution(inputFile):
    targetPresents = getInputData(inputFile)
    targetDivSum = targetPresents/10

    result = 1
    houseNumber = 1
    while result < targetDivSum:
        result = calculateDivSum(houseNumber)
        log(houseNumber, result)
        houseNumber+=1


    log(red(1500012))

    return (result, EXPECTED_RESULT)