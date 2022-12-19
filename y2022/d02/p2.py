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
 
EXPECTED_RESULT = 9541

ROUND_SCORES = {
    "AX":3, # lose -> 0+C=0+3=3
    "AY":4, # draw -> 3+A=3+1=4
    "AZ":8, # win -> 6+B=6+2=8
    "BX":1, # lose -> 0+A=0+1=1
    "BY":5, # draw -> 3+B=3+2=5
    "BZ":9, # win -> 6+C=6+3=9
    "CX":2, # lose -> 0+B=0+2=2
    "CY":6, # draw -> 3+C=3+3=6
    "CZ":7, # win -> 6+A=6+1=7
}

# A for Rock, B for Paper, and C for Scissors
# X for lose, Y for draw, and Z for win
# A = 1
# B = 2 
# C = 3 
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
        result+=ROUND_SCORES[round]

    return (result,EXPECTED_RESULT)