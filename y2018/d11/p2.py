from random import randint
import sys, os, threading, numpy
from time import sleep

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = (233, 40, 13)

THREAD_COUNT = 4

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

def getMaxPowerLevel(threadName, grid, flippedGrid, offset, step):
    maxPower = grid[0][0]
    result= (1, 1, 1, maxPower)

    for startY in range(offset, GRID_LINES, step):
        for startX in range(GRID_LINES):
            localPower = grid[startY][startX]

            if localPower>maxPower:
                maxPower = localPower
                result = (startX+1, startY+1, 1, maxPower)

            for size in range(2, GRID_LINES-max(startY,startX)+1):
                lastColumn = flippedGrid[startX+size-1][startY:startY+size-1]
                lastLine = grid[startY+size-1][startX:startX+size]

                localPower += sum(lastColumn) + sum(lastLine)

                if localPower>maxPower:
                    maxPower = localPower
                    result = (startX+1, startY+1, size, maxPower)

    return result

class SquarePowerSumThread (threading.Thread):
   def __init__(self, threadId, grid, flippedGrid, offset, step):
      threading.Thread.__init__(self)
      self.threadId = threadId
      self.grid = grid
      self.flippedGrid = flippedGrid
      self.offset = offset
      self.step = step
      self.result = None
      
   def run(self):
      self.result = getMaxPowerLevel(self.threadId, self.grid, self.flippedGrid, self.offset, self.step)



def solution(inputFile):

    serialNumber = getInputData(inputFile)
    # serialNumber = 42

    grid = matrixUtils.generate(GRID_COLS,GRID_LINES,0)

    # calculate power levels
    for lineIndex in range(GRID_LINES):
        for colIndex in range(GRID_COLS):
            grid[lineIndex][colIndex] = calculatePowerLevel(lineIndex, colIndex, serialNumber)

    flippedGrid = matrixUtils.flipMainDiagonal(grid)

    # find square with largest power
    threads = []
    for offset in range(THREAD_COUNT):
        t = SquarePowerSumThread("Thread %d"%offset, grid, flippedGrid, offset, THREAD_COUNT)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    results = []
    for t in threads:
        results.append(t.result)

    results.sort(key=lambda e: e[3], reverse=True)
    
    return (results[0][:3],EXPECTED_RESULT)