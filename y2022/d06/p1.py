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
 
EXPECTED_RESULT = 1892

def getInputData(inputFile):
    raw = getStrings(inputFile)[0]
    
    processed=raw

    return processed 

def solution(inputFile):
    signal = getInputData(inputFile)

    result=None
    for i in range(0, len(signal)-4):
        marker = list(signal[i:i+4])
        marker.sort()

        if marker[0]!=marker[1] and marker[1]!=marker[2] and marker[2]!=marker[3]:
            result = i+4
            break

    return (result,EXPECTED_RESULT)