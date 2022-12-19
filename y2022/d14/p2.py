import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 25161

SAND_SOURCE_y = 0
SAND_SOURCE_x = 500

PADDING_MULTIPLIER = 2.7

def convertCoords(coords):
    tkns = coords.split(',')
    return [int(tkns[1]),int(tkns[0])] 

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' -> ')
    
    processed = []

    for line in raw:
        processed.append([convertCoords(coords) for coords in line])

    return processed 

def drawCave(cave):
    logMatrix(cave, highlightElem=lambda e : light('S') if e =='S' else green(C_BLOCK) if e =='#' else C_DOT_FULL if e =='s' else ' ')

def solution(inputFile):
    formations = getInputData(inputFile)

    sandSourceX = SAND_SOURCE_x

    # calculate the min and max of X and Y to translate matrix to 0,0 and learn matrix size
    maxY = formations[0][0][0]
    minX = maxX = SAND_SOURCE_x

    for formation in formations:
        for coord in formation:
            minX = min(minX, coord[1])
            maxY = max(maxY, coord[0])
            maxX = max(maxX, coord[1])

    caveHorizontalPadding = int(PADDING_MULTIPLIER*(maxX-minX+1))

    # translate all coordinates and sand position
    for formation in formations:
        for coord in formation:
            coord[1]=coord[1]-minX+caveHorizontalPadding

    sandSourceX=sandSourceX-minX+caveHorizontalPadding

    # generate cave (+1 space)
    cave = matrixUtils.generate(maxY+2, maxX-minX+1+2*caveHorizontalPadding, '.')

    # add floor
    cave.append(["#" for ci in range(len(cave[0]))])

    # generate formations
    for formation in formations:
        for coordIndex in range(0,len(formation)-1):
            start = formation[coordIndex]
            stop = formation[coordIndex+1]

            for li in range(min(start[0], stop[0]), max(start[0], stop[0])+1):
                for ci in range(min(start[1], stop[1]), max(start[1], stop[1])+1):
                    cave[li][ci] = '#'

    cave[SAND_SOURCE_y][sandSourceX] = 'S'

    # drawCave(cave)

    sandUnitCounter = 0

    # while sand is not blocked
    isSandBlocked = False
    while not isSandBlocked:

        # create new sand unit 
        sandY = SAND_SOURCE_y
        sandX = sandSourceX

        sandUnitCounter+=1

        while True:
            # fall while there is space directly below unit
            while cave[sandY+1][sandX] == '.':
                sandY+=1

            if cave[sandY+1][sandX-1] == '.':
                # roll to the left
                sandX -= 1
                sandY += 1

            elif cave[sandY+1][sandX+1] == '.':
                # roll to the right
                sandX += 1
                sandY += 1
            else:
                # settled or blocked
                if cave[sandY][sandX] == 's':
                    isSandBlocked = True
                else:
                    cave[sandY][sandX] = 's'
                break
            
    # drawCave(cave)

    result = sandUnitCounter-1
    return (result,EXPECTED_RESULT)