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
NEXT_MOVES = [(0,1), (1,0), (0,0), (-1,0), (0,-1)]
DEFAULT_TENT_DISTANCE = 1000

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

def cloneStormCoords(stormCoords):
    return [stormCoord.copy() for stormCoord in stormCoords]

def getDistance(start, stormCoordHistory, map, destinationY, destinationX):

    visited = [start]
    unvisited = [start]

    goal = 10
    while len(unvisited)>0:
        currentNode = unvisited.pop(0)

        minute = currentNode[0]

        if minute == goal:
            log(minute)
            goal+=10

        for (yDelta, xDelta) in NEXT_MOVES:
            nY = currentNode[1] + yDelta
            nX = currentNode[2] + xDelta

            if map[nY][nX]=='.':
                newNode = [minute+1, nY, nX]

                if nY == destinationY and nX == destinationX:
                    return newNode


                if not [nY, nX] in stormCoordHistory[(minute+1)%len(stormCoordHistory)] and not newNode in visited:
                    unvisited.append(newNode)
                    visited.append(newNode)

    return None

def solution(inputFile):
    (map, stormCoords, stormDirections, portals) = getInputData(inputFile)

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

    toDestination = getDistance((0,1,2), stormCoordHistory, map, len(map)-2, len(map[0])-3)
    log("Reached destination. Going back...",toDestination)
    toSource = getDistance(toDestination, stormCoordHistory, map, 1, 2)
    log("Reached source. Going back...",toSource)
    toDestinationAgain = getDistance(toSource, stormCoordHistory, map, len(map)-2, len(map[0])-3)
    log("Reached destination.",toDestinationAgain)

    return toDestinationAgain[0]