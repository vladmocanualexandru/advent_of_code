import sys, os, math
from threading import local

from numpy import power

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = (235, 85)

GRID_COLS = 300
GRID_LINES = 300

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=raw[0]

    return processed 

def calculatePowerLevel(lineIndex, colIndex, serialNumber):
    lineIndex+=1
    colIndex+=1
    
    rackId = colIndex+10
    powerLevel = (rackId * lineIndex + serialNumber)*rackId

    if powerLevel<100:
        powerLevel = 0
    else:
        powerLevel = int(str(powerLevel)[-3])

    powerLevel-=5

    return powerLevel

def solution(inputFile):
    serialNumber = getInputData(inputFile)

    # log('input', serialNumber)

    grid = matrixUtils.generate(GRID_COLS,GRID_LINES,0)

    # calculate power levels
    for lineIndex in range(GRID_LINES):
        for colIndex in range(GRID_COLS):
            grid[lineIndex][colIndex] = calculatePowerLevel(lineIndex, colIndex, serialNumber)

    # find square with largest power
    maxPower = None
    result=None

    for lineIndex in range(1,GRID_LINES-1):
        for colIndex in range(1,GRID_COLS-1):
            localPower = sum(matrixUtils.getNeighbors8(grid,lineIndex,colIndex,True))
            if maxPower == None or localPower>maxPower:
                maxPower = localPower
                result = (colIndex,lineIndex)

    return (result,EXPECTED_RESULT)