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

EXPECTED_RESULT = 776160

MAX_HOUSES = pow(10,6)
 
def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)

    return raw[0] 

def solution(inputFile):
    targetPresents = getInputData(inputFile)
    targetSum = targetPresents/10

    houses = [0 for i in range(MAX_HOUSES)]

    for elfJump in range(1,MAX_HOUSES, 1):
        for houseNumber in range(elfJump, MAX_HOUSES, elfJump):
            houses[houseNumber] += elfJump

    result = None
    for houseI in range(MAX_HOUSES):
        if houses[houseI]>=targetSum:
            result = houseI
            break

    return (result, EXPECTED_RESULT)