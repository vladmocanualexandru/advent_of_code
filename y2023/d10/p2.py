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

EXPECTED_RESULT = 443

RENDER_MAP = {
    "S": C_DOT_FULL,
    
    "|": C_VERT_LINE,
    "L": C_NE_CORNER,
    "J": C_NW_CORNER,
    "F": C_SE_CORNER,
    "7": C_SW_CORNER,
    "-": C_HORIZ_LINE,
    ".": '.',
    "x": yellow('x'),
    "+": C_BLOCK
}

FLOW_MAP = {
    "N":{
        "|":"N",
        "L":"W",
        "J":"E"
    },
    "E":{
        "F":"N",
        "-":"E",
        "L":"S"
    },
    "S":{
        "F":"W",
        "7":"E",
        "|":"S",
    },
    "W":{
        "-":"W",
        "7":"N",
        "J":"S"
    }
}
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')
    
    processed=[entry for entry in raw]

    return processed 

def fillAreaX(y,x,map):
    if map[y][x] == '.':
        map[y][x] = 'x'

        for neighbor in matrixUtils.getNeighbors4(map, y,x, False, 1, True):
            fillAreaX(neighbor[1][0], neighbor[1][1], map)

def solution(inputFile):
    # read map, wrap in 1 layer to ensure existance of outside space
    map = matrixUtils.wrap(getInputData(inputFile),'.',1)

    # find ref location
    (startY, startX) = matrixUtils.find(map, returnCondition=lambda e:e=='S')[0]

    # based on symbol, find initial directions
    startDirections = []
    
    if map[startY-1][startX] in FLOW_MAP["S"]:
        startDirections.append("S")
    if map[startY+1][startX] in FLOW_MAP["N"]:
        startDirections.append("N")
    if map[startY][startX-1] in FLOW_MAP["E"]:
        startDirections.append("E")
    if map[startY][startX+1] in FLOW_MAP["W"]:
        startDirections.append("W")

    if 'E' in startDirections and 'N' in startDirections:
        map[startY][startX] = '7'
    elif 'E' in startDirections and 'S' in startDirections:
        map[startY][startX] = 'J'
    elif 'E' in startDirections and 'W' in startDirections:
        map[startY][startX] = '-'
    elif 'N' in startDirections and 'S' in startDirections:
        map[startY][startX] = '|'
    elif 'N' in startDirections and 'W' in startDirections:
        map[startY][startX] = 'F'
    elif 'S' in startDirections and 'W' in startDirections:
        map[startY][startX] = 'L'

    # using one of the directions, build the cycle
    cycleCoords = [(startY, startX)]

    direction = startDirections[0]
    x = startX
    y = startY

    while (True):
        if direction == "S":
            y-=1
        elif  direction == "N":
            y+=1
        elif  direction == "W":
            x+=1
        else:
            x-=1

        if x == startX and y == startY:
            break

        cycleCoords.append((y,x))
       
        direction = FLOW_MAP[direction][map[y][x]]

    # replace elements foreign to the main cycle with empty space
    for y in range(len(map)):
        for x in range(len(map[0])):
            if not (y,x) in cycleCoords:
                map[y][x] = '.'

    # walk the cycle and mark any open spot on the right hand side as inside
    orientation = 'N'
    if 'N' in startDirections:
        orientation = 'E'
        if 'E' in startDirections:
            orientation = 'S'

    x = startX
    y = startY

    internalLocations = []
    while (True):
        if orientation == 'N':
           if map[y][x+1] == '.':
               map[y][x+1] = 'x'
               internalLocations.append((y,x+1))

           y-=1
        elif orientation == 'E':
           if map[y+1][x] == '.':
               map[y+1][x] = 'x'
               internalLocations.append((y+1,x))

           x+=1
        elif orientation == 'S':
           if map[y][x-1] == '.':
               map[y][x-1] = 'x'
               internalLocations.append((y,x-1))

           y+=1
        else:
           if map[y-1][x] == '.':
               map[y-1][x] = 'x'
               internalLocations.append((y-1,x))

           x-=1

        if x == startX and y == startY:
            break

        if map[y][x] == 'F':
            if orientation == 'N':
                orientation = 'E'
            elif orientation == 'W':
                if map[y-1][x] == '.':
                    map[y-1][x] = 'x'
                    internalLocations.append((y-1,x))
                orientation = 'S'
        elif map[y][x] == '7':
            if orientation == 'N':
                if map[y][x+1] == '.':
                    map[y][x+1] = 'x'
                    internalLocations.append((y,x+1))
                orientation = 'W'
            elif orientation == 'E':
                orientation = 'S'
        elif map[y][x] == 'J':
            if orientation == 'S':
                orientation = 'W'
            elif orientation == 'E':
                if map[y+1][x] == '.':
                    map[y+1][x] = 'x'
                    internalLocations.append((y+1,x))
                orientation = 'N'
        elif map[y][x] == 'L':
            if orientation == 'S':
                if map[y][x-1] == '.':
                    map[y][x-1] = 'x'
                    internalLocations.append((y,x-1))
                orientation = 'E'
            elif orientation == 'W':
                orientation = 'N'

    # find every internal x and search for immediate unmarked neighbors 
    allCellsMarked = False
    while not allCellsMarked:
        allCellsMarked = True

        # unmarked neighbors are added to the list to be verified during next iteration
        moreInternalLocations = []
        for (iLy, iLx) in internalLocations:
            if map[iLy-1][iLx] == '.':
                map[iLy-1][iLx] = 'x'
                allCellsMarked = False
                moreInternalLocations.append((iLy-1, iLx))
            if map[iLy+1][iLx] == '.':
                map[iLy+1][iLx] = 'x'
                allCellsMarked = False
                moreInternalLocations.append((iLy+1, iLx))
            if map[iLy][iLx-1] == '.':
                map[iLy][iLx-1] = 'x'
                allCellsMarked = False
                moreInternalLocations.append((iLy, iLx-1))
            if map[iLy][iLx+1] == '.':
                map[iLy][iLx+1] = 'x'
                allCellsMarked = False
                moreInternalLocations.append((iLy, iLx+1))

        internalLocations += moreInternalLocations

    # count number of 'x'    
    result = len(internalLocations)

    # log(red())
    return (result, EXPECTED_RESULT)