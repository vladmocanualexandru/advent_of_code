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
            elif mapChar in ['#','x']:
                map[lineIndex][colIndex] = mapChar

                if mapChar == '#':
                    if lineIndex==1:
                        portals[(lineIndex,colIndex)] = [len(originalMap)-3, colIndex]
                    elif lineIndex == len(originalMap)-2:
                        portals[(lineIndex,colIndex)] = [2, colIndex]
                    elif colIndex == 1:
                        portals[(lineIndex,colIndex)] = [lineIndex, len(originalMap[0])-3]
                    elif colIndex == len(originalMap[0])-2:
                        portals[(lineIndex,colIndex)] = [lineIndex, 2]
                    # else:
                    #     # normal positions are portals to themselves - might be an optimization point
                    #     portals[(lineIndex,colIndex)] = (lineIndex, colIndex)

    

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

def moveStorm(stormCoord, stormDirection, portals):

    stormCoord[0] = stormCoord[0] + stormDirection[0]
    stormCoord[1] = stormCoord[1] + stormDirection[1]

    if (stormCoord[0],stormCoord[1]) in portals:
        portalCoord = portals[(stormCoord[0],stormCoord[1])]
        stormCoord[0] = portalCoord[0]
        stormCoord[1] = portalCoord[1]

NEXT_MOVES = [(0,1,0), (1,0,0), (0,0,0), (-1,0,0), (0,-1,0)]

def getOptions(map, stormCoords, myY, myX,destinationY,destinationX):
    options = []

    for (deltaY,deltaX,priorityBonus) in NEXT_MOVES:
        optionY = myY+deltaY
        optionX = myX+deltaX

        if map[optionY][optionX] == '.' and not [optionY,optionX] in stormCoords:
            priority = priorityBonus+geometryUtils.get2DDistance(destinationY,destinationX,optionY,optionX)
            options.append([optionY,optionX,priority])


    return options

def cloneStormCoords(stormCoords):
    return [stormCoord.copy() for stormCoord in stormCoords]



def navigate(minute, minMinutes, myY, myX, destinationY, destinationX, map, stormCoordHistory, stormPositionHistory):
    log(geometryUtils.get2DDistance(myY, myX, destinationY, destinationX))

    stormIndex = minute%len(stormCoordHistory)

    if minute >= minMinutes:
        stormPositionHistory.append((myY, myX, stormIndex))
        return minute

    if myY == destinationY and myX == destinationX:
        log(green("Reached destination @minute", minute))
        stormPositionHistory.append((myY, myX, stormIndex))
        return minute

    options = getOptions(map, stormCoordHistory[stormIndex], myY, myX, destinationY, destinationX)
    options.sort(key=lambda e:e[2])
    
    if options == []:
        # log(red("Blocked by storms"))
        stormPositionHistory.append((myY, myX, stormIndex))
        return DEFAULT_MIN_MINUTE_VALUE
    else:
        for [optionY, optionX, priority] in options:
        # for [optionY, optionX] in options:
            if not ((optionY, optionX, stormIndex) in stormPositionHistory):
                minMinutes = min(minMinutes,navigate(minute+1, minMinutes, optionY, optionX, destinationY, destinationX, map, stormCoordHistory,stormPositionHistory))

        stormPositionHistory.append((optionY, optionX, stormIndex))
        return minMinutes

def solution(inputFile):
    (map, stormCoords, stormDirections, portals) = getInputData(inputFile)

    height = len(map)
    width = len(map[0])

    myY,myX = (1,2) 
    destinationY,destinationX = (height-2,width-3) 

    stormCoordHistory = [cloneStormCoords(stormCoords)]

    minuteCounter = 0
    while True:
        for stormIndex in range(len(stormCoords)):
            moveStorm(stormCoords[stormIndex],stormDirections[stormIndex],portals)

        minuteCounter +=1

        if stormCoords in stormCoordHistory:
            log('Found pattern @ minute', minuteCounter)
            break
        else:
            stormCoordHistory.append(cloneStormCoords(stormCoords))

    log(red(434, 151, 396, 392, 345, 324))

    navigate(0, DEFAULT_MIN_MINUTE_VALUE, myY, myX, destinationY, destinationX, map, stormCoordHistory,[])

    return None