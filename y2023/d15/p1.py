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

EXPECTED_RESULT = 506891
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile,",")
    
    processed=[entry for entry in raw]

    return processed[0] 

def solution(inputFile):
    result = 0
    
    steps = getInputData(inputFile)

    for step in steps:
        hashValue = 0
        for c in step:
            hashValue=(hashValue+ord(c))*17%256

        result+=hashValue

    # log(red())
    return (result, EXPECTED_RESULT)