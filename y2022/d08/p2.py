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
 
EXPECTED_RESULT = 268464

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, '')
    
    processed=raw

    return processed 

def solution(inputFile):
    treeMatrix = getInputData(inputFile)
    mSize = len(treeMatrix)

    visibleMatrixW = matrixUtils.generate(mSize, mSize, 0)
    visibleMatrixN = matrixUtils.generate(mSize, mSize, 0)
    visibleMatrixE = matrixUtils.generate(mSize, mSize, 0)
    visibleMatrixS = matrixUtils.generate(mSize, mSize, 0)

    allVisMats = [visibleMatrixW, visibleMatrixS, visibleMatrixE, visibleMatrixN]

    for rotIndex in range(4):
        # if a tree is higher than the tree to the left, it's higher than all the tree that tree is higher than :D
        for lineIndex in range(mSize):
            for colIndex in range(1,mSize):
                visibleTrees = 0
                for revColIndex in range(colIndex-1, -1, -1):
                    visibleTrees+=1
                    if treeMatrix[lineIndex][revColIndex]>=treeMatrix[lineIndex][colIndex]:
                        break

                allVisMats[rotIndex][lineIndex][colIndex] = visibleTrees

        # rotate matrix
        treeMatrix = matrixUtils.rotate(treeMatrix)

    visibleMatrixS = matrixUtils.rotate(visibleMatrixS, cw=False)
    visibleMatrixE = matrixUtils.rotate(visibleMatrixE, times=2)
    visibleMatrixN = matrixUtils.rotate(visibleMatrixN)

    resultMatrix = matrixUtils.generate(mSize, mSize, -1)
    
    for lineIndex in range(mSize):
        for colIndex in range(mSize):
            value = visibleMatrixN[lineIndex][colIndex]
            value *= visibleMatrixE[lineIndex][colIndex]
            value *= visibleMatrixS[lineIndex][colIndex]
            value *= visibleMatrixW[lineIndex][colIndex]

            resultMatrix[lineIndex][colIndex] = value

    result = matrixUtils.agg(resultMatrix, max)

    return (result,EXPECTED_RESULT)