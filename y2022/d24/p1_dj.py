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

def cloneStormCoords(stormCoords):
    return [stormCoord.copy() for stormCoord in stormCoords]

def isFree(y, x, minute, stormCoordHistory):
    return not [y,x] in stormCoordHistory[minute]

def getNeighbors(y,x,map):
    neighbors = [] 
    for (yDelta, xDelta) in NEXT_MOVES:
        nY = y + yDelta
        nX = x + xDelta
        if 1<=nY<=(len(map)-2) and 1<=nX<=(len(map[0])-2) and map[nY][nX]=='.':
            neighbors.append((nY,nX))


    return neighbors

def generateNodeLabel(y,x,minuteCounter):
    return "%s_%s_%s" % (y,x,minuteCounter)

def getDistanceToDestination(start, nodes, layers):

    unvisited = []
    tentDists = []
    for node in nodes:
        # log(node, nodes[node])
        unvisited.append(node)
        tentDists.append(DEFAULT_TENT_DISTANCE)

    tentDists[unvisited.index(start)] = 0

    # unvisited.sort(key=lambda e:nodes[e]["tentDist"])

    minTentDist = min(tentDists)
    minIndex = tentDists.index(minTentDist)

    logGoal = 10
    while len(unvisited)>0 and minTentDist<DEFAULT_TENT_DISTANCE:
        currentNode = nodes[unvisited[minIndex]]
        # log(currentNode)
        if minTentDist==logGoal:
            log(minTentDist)
            logGoal+=10

        if currentNode["isDestination"]:
            return minTentDist

        for connection in currentNode["connections"]:
            connectionIndex = unvisited.index(connection)
            tentDists[connectionIndex] = min(tentDists[connectionIndex], minTentDist+1)

        unvisited.pop(minIndex)
        tentDists.pop(minIndex)

        minTentDist = min(tentDists)
        minIndex = tentDists.index(minTentDist)

    return None

def solution(inputFile):
    (map, stormCoords, stormDirections, portals) = getInputData(inputFile)

    height = len(map)
    width = len(map[0])

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

    stormMap = [matrixUtils.generate(height,width,0) for stormCounter in range(len(stormCoordHistory))]

    for stormCounter in range(len(stormCoordHistory)):
        for (y,x) in stormCoordHistory[stormCounter]:
            stormMap[stormCounter][y][x] = 1

    # based on storm model, build all y/x/minute nodes and connections between them
    nodes = {}

    for minuteCounter in range(len(stormCoordHistory)-1):
    # for minuteCounter in range(2*len(stormCoordHistory)):
        # log(minuteCounter)
        for y in range(1, height-1):
            for x in range(1, width-1):
                # if not (y,x) in stormCoordHistory[minuteCounter]:
                if stormMap[(minuteCounter%len(stormCoordHistory))][y][x]==0 and map[y][x] == '.':
                    nodes[(minuteCounter,y,x)] = {"connections":[], "isDestination":(y==height-2 and x == width-3)}
                    for (nY,nX) in getNeighbors(y,x,map):
                        if stormMap[(minuteCounter+1)%len(stormCoordHistory)][nY][nX]==0:
                            nodes[(minuteCounter,y,x)]["connections"].append((minuteCounter+1,nY,nX))

    # log(getDistanceToDestination((0,1,2), nodes, 2*len(stormCoordHistory)))    
    log(getDistanceToDestination((0,1,2), nodes, len(stormCoordHistory)-1))    

    # WRONG: 434, 151, 396, 392, 345, 324

    return None