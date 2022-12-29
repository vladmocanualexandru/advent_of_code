import sys, os, math, random
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
DIRECTIONS = {">":(0,1),"v":(1,0),"<":(0,-1),"^":(-1,0)}
DEFAULT_MIN_MINUTE_VALUE = 1000

def getInputData(inputFile):
    originalMap = matrixUtils.wrap(getTuples_text(inputFile,''),'x',1)

    map = matrixUtils.generate(len(originalMap), len(originalMap[0]), '.')
    
    stormCoords = []
    stormDirections = []

    portals = {}
    for lineIndex in range(len(originalMap)):
        for colIndex in range(len(originalMap[0])):
            mapChar = originalMap[lineIndex][colIndex]
            if mapChar in ['>','v','<','^']:
                stormCoords.append([lineIndex, colIndex])
                stormDirections.append(DIRECTIONS[mapChar])
            else:
                map[lineIndex][colIndex] = mapChar

            if lineIndex==1:
                portals[(lineIndex,colIndex)] = [len(originalMap)-3, colIndex]
            elif lineIndex == len(originalMap)-2:
                portals[(lineIndex,colIndex)] = [2, colIndex]
            elif colIndex == 1:
                portals[(lineIndex,colIndex)] = [lineIndex, len(originalMap[0])-3]
            elif colIndex == len(originalMap[0])-2:
                portals[(lineIndex,colIndex)] = [lineIndex, 2]
            else:
                portals[(lineIndex,colIndex)] = [lineIndex, colIndex]

    return (map, stormCoords, stormDirections, portals)

def vizualizeMap(map, stormCoords, myY, myX):

    cloneMap = matrixUtils.clone(map)
    for [sY,sX] in stormCoords:
        if cloneMap[sY][sX] == '.':
            cloneMap[sY][sX] = "*"
        elif cloneMap[sY][sX] == "*":
            cloneMap[sY][sX] = 2
        else:
            cloneMap[sY][sX] += 1

    cloneMap[myY][myX] = 'E'

    logMatrix(cloneMap)

NEXT_MOVES = [(0,1), (1,0), (0,0), (-1,0), (0,-1)]

def cloneStormCoords(stormCoords):
    return [stormCoord.copy() for stormCoord in stormCoords]

def isFree(y, x, minute, stormCoordHistory):
    return not [y,x] in stormCoordHistory[minute]

def solution(inputFile):
    (map, stormCoords, stormDirections, portals) = getInputData(inputFile)

    myY,myX = (1,2) 

    # build storm model while looking for cyclicity
    stormCoordHistory = [cloneStormCoords(stormCoords)]
    while True:
        # move storm
        for stormIndex in range(len(stormCoords)):
            stormCoord = stormCoords[stormIndex]
            stormDirection = stormDirections[stormIndex]

            stormCoords[stormIndex] = portals[(stormCoord[0] + stormDirection[0],stormCoord[1] + stormDirection[1])]

        # check if current configuration has been encountered before
        if stormCoords in stormCoordHistory:
            log('Found pattern @ minute', len(stormCoordHistory))
            break
        else:
            # record current storm configuration
            stormCoordHistory.append(cloneStormCoords(stormCoords))

    # based on storm model, build all y/x/minute nodes and connections between them
    nodes = {}

    for minuteCounter in range(len(stormCoordHistory)-1):
        currentStorm = stormCoordHistory[minuteCounter]

        


    log(isFree(4,2,2, stormCoordHistory))




    log(red(434, 151, 396, 392, 345, 324))

    # navigate(0, DEFAULT_MIN_MINUTE_VALUE, myY, myX, destinationY, destinationX, map, stormCoordHistory,[])

    return None