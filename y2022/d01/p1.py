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
 
EXPECTED_RESULT = 72070

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    sums = []
    sum = 0

    maxBlock = 0

    for item in inputData:
        if item == '':
            maxBlock = max(maxBlock, sum)
            sum = 0
        else:
            sum += int(item)

    maxBlock = max(maxBlock, sum)
    
    result=maxBlock

    return (result,EXPECTED_RESULT)