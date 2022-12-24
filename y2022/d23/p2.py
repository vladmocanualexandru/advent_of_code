# not the proper solution for this part - it's basically part1 solution + 10minutes :) I hope to return with a better design

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

ALL_DIRECTIONS = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

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

def isElfRelevant(x,y, elfCoords):
    for (xOffset,yOffset) in ALL_DIRECTIONS:
        if (x+xOffset, y+yOffset) in elfCoords:
            return True

    return False

def solution(inputFile):
    elfCoords = getInputData(inputFile)

    directionOrder = ["N","S","W","E"]

    roundNo = 0
    elfMoved= True
    while elfMoved:
        roundNo+=1

        possibleMoves = {}
        cancelledMoves = []

        elfMoved= False
        relevantElves = len(elfCoords)
        for (x,y) in elfCoords:
            if isElfRelevant(x,y,elfCoords):
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

            else:
                relevantElves-=1

        for possibleMove in possibleMoves:
            elfCoords.remove(possibleMoves[possibleMove])
            elfCoords.append((possibleMove[0],possibleMove[1]))

            elfMoved = True
        
        directionOrder.append(directionOrder[0])
        directionOrder.pop(0)


    return roundNo