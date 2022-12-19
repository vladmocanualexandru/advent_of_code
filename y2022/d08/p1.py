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
 
EXPECTED_RESULT = 1713

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, '')
    
    processed=raw

    return processed 

def solution(inputFile):
    treeMatrix = getInputData(inputFile)
    mSize = len(treeMatrix)
    
    hiddenMatrix = matrixUtils.wrap(matrixUtils.generate(mSize-2, mSize-2, 1), 0, 1)

    # matrixUtils.log(treeMatrix, '', log)
    # log('--')



    for rotIndex in range(4):
        # select hidden trees candidates
        candidates = matrixUtils.find(hiddenMatrix, returnCondition=lambda e : e==1)
        
        # look for visible trees
        for (y,x) in candidates:
            if treeMatrix[y][x] > max(treeMatrix[y][:x]):
                hiddenMatrix[y][x] = 0

        # rotate matrix
        treeMatrix = matrixUtils.rotate(treeMatrix)
        hiddenMatrix = matrixUtils.rotate(hiddenMatrix)

    # matrixUtils.log(hiddenMatrix, '', log)

    result=pow(mSize,2) - matrixUtils.agg(hiddenMatrix, sum)

    return (result,EXPECTED_RESULT)