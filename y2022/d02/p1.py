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
 
EXPECTED_RESULT = 10595

ROUND_SCORES = {
    "AX":3,
    "AY":6,
    "AZ":0,
    "BX":0,
    "BY":3,
    "BZ":6,
    "CX":6,
    "CY":0,
    "CZ":3,
}

CHOICE_SCORES = {
    "X":1,
    "Y":2,
    "Z":3,
}

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# X = 1
# Y = 2 
# Z = 3 
# loss = 0 
# tie = 3
# win = 6


def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[r.replace(' ','') for r in raw]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    result=0

    for round in inputData:
        result+=ROUND_SCORES[round] + CHOICE_SCORES[round[1]]

    return (result,EXPECTED_RESULT)