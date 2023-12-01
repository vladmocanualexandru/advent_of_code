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

EXPECTED_RESULT = 54630
 
def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=[[int(elem) for elem in entry if elem.isdigit()] for entry in raw]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    # log(inputData)

    result = 0
    for entry in inputData:
        result += entry[0]*10 + entry[-1]


    return (result, EXPECTED_RESULT)