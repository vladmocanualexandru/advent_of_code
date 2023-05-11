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

EXPECTED_RESULT = 1006
STEPS = 100
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')

    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    grid = getInputData(inputFile)

    height = len(grid)
    width = len(grid[0])

    for stepCounter in range(STEPS):
        newGrid = matrixUtils.generate(height, width, '.')
        newGrid[0][0] = newGrid[0][width-1] = newGrid[height-1][0] = newGrid[height-1][width-1] = '#'

        for lineIndex in range(height):
            for colIndex in range(width):

                if (lineIndex == 0 and colIndex==0) or (lineIndex == 0 and colIndex==width-1) or (lineIndex == height-1 and colIndex==0) or (lineIndex == height-1 and colIndex==width-1):
                    continue
                
                neighborCount = sum([1 if n =='#' else 0 for n in matrixUtils.getNeighbors8(grid, lineIndex, colIndex)])

                if grid[lineIndex][colIndex] == '#':
                    newGrid[lineIndex][colIndex] = '#' if (neighborCount==2 or neighborCount==3) else '.'
                else:
                    newGrid[lineIndex][colIndex] = '#' if neighborCount==3 else '.'

        grid = newGrid

    # matrixUtils.log(grid, log)
    # matrixUtils.log(grid, log, '', lambda e: ' ' if e == '.' else color(C_BLOCK))
    # log(' ')

    result = matrixUtils.addAll(grid, lambda e: e=='#', lambda e: 1)
    return (result, EXPECTED_RESULT)