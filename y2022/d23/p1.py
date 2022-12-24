import sys, os, math
import numpy as np
import pandas as pd

from functools import cmp_to_key

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

ROUND_COUNT = 10

DIRECTIONS = {
    "N": [(-1,-1),(0,-1),(1,-1)],
    "E": [(1,-1),(1,0),(1,1)],
    "S": [(-1,1),(0,1),(1,1)],
    "W": [(-1,-1),(-1,0),(-1,1)],
}

def compareCoords(a,b):
    if a[1]!=b[1]:
        return a[1]-b[1]
    else:
        return a[0]-b[0]
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')

    processed = []
    for lineIndex in range(len(raw)):
        for colIndex in range(len(raw[lineIndex])):
            if raw[lineIndex][colIndex] == '#':
                processed.append((colIndex, lineIndex))
    
    return processed 

def solution(inputFile):
    elfCoords = getInputData(inputFile)

    # elfCoords.sort(key=cmp_to_key(compareCoords))

    # log(elfCoords)

    directionOrder = ["N","S","W","E"]

    for roundNo in range(ROUND_COUNT):

        possibleMoves = {}
        cancelledMoves = []
        for (x,y) in elfCoords:

            elfHasNeighbors = False
            possibleMove = None
            for directionIndex in range(4):
                directionData = DIRECTIONS[directionOrder[directionIndex]]

                for directionOffsetIndex in range(3):
                    directionOffset = directionData[directionOffsetIndex]
                    if (x+directionOffset[0],y+directionOffset[1]) in elfCoords:
                        elfHasNeighbors = True
                        break
                else:
                    if possibleMove == None:
                        possibleMove = (x+directionData[1][0],y+directionData[1][1])

                if elfHasNeighbors and possibleMove != None:
                    break

            if elfHasNeighbors and possibleMove != None and not possibleMove in cancelledMoves:
                if possibleMove in possibleMoves:
                    cancelledMoves.append(possibleMove)
                    del possibleMoves[possibleMove]
                else:
                    possibleMoves[possibleMove] = (x,y)

        for possibleMove in possibleMoves:
            elfCoords.remove(possibleMoves[possibleMove])
            elfCoords.append((possibleMove[0],possibleMove[1]))
        
        directionOrder.append(directionOrder[0])
        directionOrder.pop(0)

    elfCoords.sort(key=cmp_to_key(compareCoords))

    (minX,minY) = (elfCoords[0][0],elfCoords[0][1])
    (maxX,maxY) = (elfCoords[0][0],elfCoords[0][1])

    for (x,y) in elfCoords[1:]:
        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)

    # translatedElfCoords = []
    # for (x,y) in elfCoords[0:]:
    #     translatedElfCoords.append((x-minX, y-minY))

    # log(translatedElfCoords)

    # log(minX,maxX,minY,maxY)
    result = (maxX-minX+1)*(maxY-minY+1) - len(elfCoords)

    return result