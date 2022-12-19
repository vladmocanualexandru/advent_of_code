import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 29839

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[(entry[0], int(entry[1:])) for entry in raw]

    return processed 

def solution(inputFile):
    instructions = getInputData(inputFile)

    shipX = shipY = 0

    waypointDeltaX = 10
    waypointDeltaY = 1

    for (c,v) in instructions:
        # log(c,v)

        if c == 'F':
            shipX+=v*waypointDeltaX
            shipY+=v*waypointDeltaY
        elif c == 'N':
            waypointDeltaY+=v
        elif c == 'S':
            waypointDeltaY-=v
        elif c == 'E':
            waypointDeltaX+=v
        elif c == 'W':
            waypointDeltaX-=v
        else:
            v = int(v/90)

            if c == 'R':
                v = 4-v

            newX = waypointDeltaX*-1
            newY = waypointDeltaY*-1

            if v == 1:
                newY = waypointDeltaX
                newX = waypointDeltaY*-1
            elif v == 3:
                newY=waypointDeltaX*-1
                newX=waypointDeltaY
            
            (waypointDeltaX,waypointDeltaY) = (newX, newY)


        # log("ship ",shipX,shipY)
        # log("waypoint ",waypointDeltaX,waypointDeltaY)

    result=abs(shipX) + abs(shipY)

    return (result,EXPECTED_RESULT)