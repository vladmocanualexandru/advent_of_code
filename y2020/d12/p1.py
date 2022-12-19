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
 
EXPECTED_RESULT = 2847

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[(entry[0], int(entry[1:])) for entry in raw]

    return processed 

def navigate(x,y,direction,value):
    if direction == 'N':
        y+=value
    elif direction == 'E':
        x+=value
    elif direction == 'S':
        y-=value
    elif direction == 'W':
        x-=value

    return (x,y)

def solution(inputFile):
    instructions = getInputData(inputFile)

    directions = ['E', 'S', 'W', 'N']
    
    directionIndex = 0
    shipX = shipY = 0

    for (c,v) in instructions:
        if c == 'R':
            directionIndex=(directionIndex+int(v/90))%4
        elif c == 'L':
            directionIndex=(directionIndex-int(v/90))%4
        elif c == 'F':
            (shipX, shipY) = navigate(shipX, shipY, directions[directionIndex],v)
        else: 
            (shipX, shipY) = navigate(shipX, shipY, c, v)


    result=abs(shipX) + abs(shipY)

    return (result,EXPECTED_RESULT)