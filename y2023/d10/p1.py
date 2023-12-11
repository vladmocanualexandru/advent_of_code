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

EXPECTED_RESULT = 6979

RENDER_MAP = {
    "|*": C_VERT_LINE,
    "L*": C_NE_CORNER,
    "J*": C_NW_CORNER,
    "F*": C_SE_CORNER,
    "7*": C_SW_CORNER,
    "-*": C_HORIZ_LINE,
    "S*": C_DOT_FULL,
    
    "|": C_VERT_LINE,
    "L": C_NE_CORNER,
    "J": C_NW_CORNER,
    "F": C_SE_CORNER,
    "7": C_SW_CORNER,
    "-": C_HORIZ_LINE,
    ".": ' '
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

def solution(inputFile):
    map = matrixUtils.wrap(getInputData(inputFile),'.',1)

    (startY, startX) = matrixUtils.find(map, returnCondition=lambda e:e=='S')[0]

    startDirections = []
    
    if map[startY-1][startX] in FLOW_MAP["S"]:
        startDirections.append("S")
    if map[startY+1][startX] in FLOW_MAP["N"]:
        startDirections.append("N")
    if map[startY][startX-1] in FLOW_MAP["E"]:
        startDirections.append("E")
    if map[startY][startX+1] in FLOW_MAP["W"]:
        startDirections.append("W")

    coordLength = {}
    coordLength[(startY, startX)] = 0

    for direction in startDirections:
        x = startX
        y = startY

        # log(purple(y,x,direction))
        routeLength = 0
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

            routeLength += 1

            if not (y,x) in coordLength:
                coordLength[(y, x)] = routeLength
            else:
                coordLength[(y, x)] = min(routeLength, coordLength[(y, x)])

            direction = FLOW_MAP[direction][map[y][x]]

    result = max([coordLength[coord] for coord in coordLength]) 

    # fancy rendering
    # for y in range(len(map)):
    #     for x in range(len(map[0])):
    #         if (y,x) in coordLength:
    #             map[y][x] += "*"
    

    # logMatrix(map, highlightElem=lambda e: redBG(RENDER_MAP[e]) if e == "S*" else cyan(RENDER_MAP[e]) if e[-1]=='*' else dark(RENDER_MAP[e]))
    

    # log(red())
    return (result, EXPECTED_RESULT)