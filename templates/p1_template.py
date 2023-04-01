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
    raw = getRawLines(inputFile)
    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    log(inputData)

    result = None
    return (result, EXPECTED_RESULT)