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

EXPECTED_RESULT = 1061
STEPS = 100
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')

    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    grid = getInputData(inputFile)

    for stepCounter in range(STEPS):
        newGrid = matrixUtils.generate(len(grid), len(grid[0]), '.')

        for lineIndex in range(len(grid)):
            for colIndex in range(len(grid[0])):
                neighborCount = sum([1 if n =='#' else 0 for n in matrixUtils.getNeighbors8(grid, lineIndex, colIndex)])
                if grid[lineIndex][colIndex] == '#':
                    newGrid[lineIndex][colIndex] = '#' if (neighborCount==2 or neighborCount==3) else '.'
                else:
                    newGrid[lineIndex][colIndex] = '#' if neighborCount==3 else '.'

        grid = newGrid

    # matrixUtils.log(grid, log, '', lambda e: ' ' if e == '.' else color(C_BLOCK))

    result = matrixUtils.addAll(grid, lambda e: e=='#', lambda e: 1)
    return (result, EXPECTED_RESULT)