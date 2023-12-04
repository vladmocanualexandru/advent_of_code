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

EXPECTED_RESULT = 26346

def convertToNumbers(strArr):
    return [int(entry) for entry in strArr if entry.isnumeric()]
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' | ')
    
    processed=[(convertToNumbers(entry[0].split(' ')[2:]), convertToNumbers(entry[1].split(' '))) for entry in raw]

    return processed 

def solution(inputFile):
    result = 0

    cards = getInputData(inputFile)

    for card in cards:
        winningNumbers = [number for number in card[0] if number in card[1]]
        if len(winningNumbers)>0:
            result += pow(2, len(winningNumbers)-1)

    return (result, EXPECTED_RESULT)