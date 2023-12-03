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

EXPECTED_RESULT = 556057
 
def getInputData(inputFile):

    raw = getTuples_text(inputFile, '')

    processed=matrixUtils.wrap(raw, '.')

    return processed 

def containsSymbol(arr):
    for elem in arr:
        if not elem.isdigit() and elem != '.':
            return True
    return False

def solution(inputFile):
    mat = getInputData(inputFile)

    lines = len(mat)
    cols = len(mat[0])
    
    result = 0

    number = 0
    numberIsRelevant = False
    for lineIndex in range(1,lines-1, 1):
        for colIndex in range(1,cols-1, 1):
            cell = mat[lineIndex][colIndex]
            if cell.isdigit():
                number*=10
                number+=int(cell)

                if not numberIsRelevant:
                    numberIsRelevant = containsSymbol(matrixUtils.getNeighbors8(mat, lineIndex, colIndex, False, 1, False))
                
            else:
                if number!=0 and numberIsRelevant:
                    result+=number

                number=0
                numberIsRelevant=False



    return (result, EXPECTED_RESULT)