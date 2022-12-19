import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 588

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'-',',')
    
    processed=[[(entry[0],entry[1]),(entry[2],entry[3])] for entry in raw]

    return processed 

def solution(inputFile):
    pairs = getInputData(inputFile)

    result=0

    for pair in pairs:
        minV = min(pair[0][0], pair[1][0])
        maxV = max(pair[0][1], pair[1][1])

        if (minV == pair[0][0] and maxV == pair[0][1]) or (minV == pair[1][0] and maxV == pair[1][1]):
            result+=1

    return (result,EXPECTED_RESULT)