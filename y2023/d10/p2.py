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

EXPECTED_RESULT = None

RENDER_MAP = {
    "S": C_DOT_FULL,
    
    "|": C_VERT_LINE,
    "L": C_NE_CORNER,
    "J": C_NW_CORNER,
    "F": C_SE_CORNER,
    "7": C_SW_CORNER,
    "-": C_HORIZ_LINE,
    ".": '.',
    "x": 'x',
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

    log("cycle coords computed")


    # replace elements foreign to the main cycle with empty space
    for y in range(len(map)):
        for x in range(len(map[0])):
            if not (y,x) in cycleCoords:
                map[y][x] = '.'

    log("map cleaned")

    
    logMatrix(map, highlightElem=lambda e: yellow(RENDER_MAP[e]) if e == "S" else cyan(RENDER_MAP[e]) if e[-1]!='.' else dark(RENDER_MAP[e]))

    # expand the map, to remove touching walls
    newMap = matrixUtils.generate(len(map)*2, len(map[0])*2, '.')

    cycleCoords = [(2*coord[0], 2*coord[1]) for coord in cycleCoords]

    fillerCoords = []
    for cCoordIndex in range(len(cycleCoords)):
        coord0 = cycleCoords[cCoordIndex]
        coord1 = cycleCoords[(cCoordIndex+1)%len(cycleCoords)]
        fillerCoord = (int((coord0[0]+coord1[0])/2),int((coord0[1]+coord1[1])/2))
        fillerCoords.append(fillerCoord)

    log("filler cycle elements computed")

    for cycleCoord in cycleCoords:
        newMap[cycleCoord[0]][cycleCoord[1]] = "+"

    for fillerCoord in fillerCoords:
        newMap[fillerCoord[0]][fillerCoord[1]] = "+"

    map = newMap

    log("expanded map built")

    # find inside cell
    insideCellCoord = None
    for y in range(len(map)):
        for x in range(len(map[0])-1):
            if map[y][x] == '+':
                if map[y][x+1] == '.':
                    insideCellCoord = (y,x+1)

                break

        if not insideCellCoord == None:
            break

    log("inside cell found")
    # map[insideCellCoord[0]][insideCellCoord[1]] = 'S'   


    # fill inside area with 'x'
    fillAreaX(insideCellCoord[0],insideCellCoord[1],map)

    log("inside area marked")
    logMatrix(map, highlightElem=lambda e: yellow(RENDER_MAP[e]) if e == "S" else cyan(RENDER_MAP[e]) if e[-1]!='.' else dark(RENDER_MAP[e]))

    # contract the map
    newMap = matrixUtils.generate(int(len(map)/2), int(len(map[0])/2), '.')
    for y in range(len(map)-1,-1,-1):
        for x in range(len(map[0])-1,-1,-1):
            newMap[int(y/2)][int(x/2)] = map[y][x]
    map = newMap 

    log("map contracted")

    logMatrix(map, highlightElem=lambda e: yellow(RENDER_MAP[e]) if e == "S" else cyan(RENDER_MAP[e]) if e[-1]!='.' else dark(RENDER_MAP[e]))

    # count number of 'x'    
    result = len(matrixUtils.find(map, returnCondition=lambda e: e == 'x'))

    # log(red())
    return (result, EXPECTED_RESULT)