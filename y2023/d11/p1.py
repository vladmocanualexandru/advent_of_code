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

EXPECTED_RESULT = 9684228
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    result = 0
    
    map = getInputData(inputFile)

    emptyLines = []
    for lineIndex in range(len(map)):
        if sum([1 if cell == '#' else 0 for cell in map[lineIndex]]) == 0:
            emptyLines.append(lineIndex)

    emptyColumns = []
    galaxyLocations = []
    for colIndex in range(len(map[0])):
        emptyColumn = True
        for lineIndex in range(len(map)):
            if map[lineIndex][colIndex] == '#':
                emptyColumn = False
                galaxyLocations.append((lineIndex, colIndex))

        if emptyColumn:
            emptyColumns.append(colIndex)

    routeCounter = 0
    for galaxyStartIndex in range(len(galaxyLocations)-1):
        for galaxyStopIndex in range(galaxyStartIndex+1, len(galaxyLocations), 1):
            routeCounter+=1
            galaxyStartLocation = galaxyLocations[galaxyStartIndex]
            galaxyStopLocation = galaxyLocations[galaxyStopIndex]

            minY = min(galaxyStartLocation[0], galaxyStopLocation[0])
            maxY = max(galaxyStartLocation[0], galaxyStopLocation[0])
            minX = min(galaxyStartLocation[1], galaxyStopLocation[1])
            maxX = max(galaxyStartLocation[1], galaxyStopLocation[1])

            distance = abs(galaxyStartLocation[0]-galaxyStopLocation[0]) + abs(galaxyStartLocation[1]-galaxyStopLocation[1])

            distance += sum([1 if emptyLine>=minY and emptyLine<=maxY else 0 for emptyLine in emptyLines])
            distance += sum([1 if emptyColumn>=minX and emptyColumn<=maxX else 0 for emptyColumn in emptyColumns])

            result += distance

    # log(red())
    return (result, EXPECTED_RESULT)