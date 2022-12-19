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
 
EXPECTED_RESULT = 805

SAND_SOURCE_x = 500

MATRIX_TOP_PADDING = 5
MATRIX_WRAP_SIZE = 1

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
    logMatrix(cave, highlightElem=lambda e : light(C_VERT_LINE) if e =='S' else red('x') if e=='x' else purple(C_BLOCK) if e =='#' else light(C_BLOCK) if e =='s' else ' ')

def solution(inputFile):
    formations = getInputData(inputFile)

    sandSourceX = SAND_SOURCE_x

    # calculate the min and max of X and Y to translate matrix to 0,0 and learn matrix size
    minY = maxY = formations[0][0][0]
    minX = maxX = formations[0][0][1]

    for formation in formations:
        for coord in formation:
            minY = min(minY, coord[0])
            minX = min(minX, coord[1])
            maxY = max(maxY, coord[0])
            maxX = max(maxX, coord[1])

    # translate all coordinates and sand position
    for formation in formations:
        for coord in formation:
            coord[0]=coord[0]-minY+MATRIX_TOP_PADDING+MATRIX_WRAP_SIZE
            coord[1]=coord[1]-minX+MATRIX_WRAP_SIZE

    sandSourceX=sandSourceX-minX+MATRIX_WRAP_SIZE

    # generate cave
    cave = matrixUtils.generate(maxY-minY+1+MATRIX_TOP_PADDING, maxX-minX+1, '.')

    # wrap cave with abyss area
    cave = matrixUtils.wrap(cave, 'x', MATRIX_WRAP_SIZE)

    # generate formations
    for formation in formations:
        for coordIndex in range(0,len(formation)-1):
            start = formation[coordIndex]
            stop = formation[coordIndex+1]

            for li in range(min(start[0], stop[0]), max(start[0], stop[0])+1):
                for ci in range(min(start[1], stop[1]), max(start[1], stop[1])+1):
                    cave[li][ci] = '#'

    cave[MATRIX_WRAP_SIZE][sandSourceX] = 'S'


    # drawCave(cave)

    sandUnitCounter = 0

    # while no sand unit reached abyss
    hasSandReachedAbyss = False
    while not hasSandReachedAbyss:

        # create new sand unit 
        sandY = MATRIX_WRAP_SIZE
        sandX = sandSourceX

        sandUnitCounter+=1

        while True:

            # fall while there is space directly below unit
            while cave[sandY+1][sandX] in ['.','x']:
                sandY+=1
                if cave[sandY][sandX] == 'x':
                    hasSandReachedAbyss = True
                    break

            if hasSandReachedAbyss:
                break

            if cave[sandY+1][sandX-1] in ['.','x']:
                # roll to the left
                sandX -= 1
                sandY += 1
                if cave[sandY][sandX] == 'x':
                    hasSandReachedAbyss = True
                    break

            elif cave[sandY+1][sandX+1] in ['.','x']:
                # roll to the right
                sandX += 1
                sandY += 1
                if cave[sandY][sandX] == 'x':
                    hasSandReachedAbyss = True
                    break
            else:
                # settled
                cave[sandY][sandX] = 's'
                break
            
    
    # drawCave(cave)

    # result contains the unit that reached abyss 1 unit must be substracted from final value
    result = sandUnitCounter-1
    return (result,EXPECTED_RESULT)