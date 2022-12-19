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
 
EXPECTED_RESULT = 5710

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')
    
    processed=[(entry[0],int(entry[1])) for entry in raw]

    return processed 

def adjustTailPos(headPos, tailPos):
    if abs(headPos[0]-tailPos[0]) == 2:
        tailPos[1] = headPos[1]
        tailPos[0] = int((headPos[0]+tailPos[0])/2)
    elif abs(headPos[1]-tailPos[1]) == 2:
        tailPos[0] = headPos[0]
        tailPos[1] = int((headPos[1]+tailPos[1])/2)

def solution(inputFile):
    moves = getInputData(inputFile)

    headPos = [0,0]
    tailPos = [0,0]

    tailPositions = [[0,0]]
    for (d,s) in moves:
        # log("head", headPos, "tail", tailPos)

        for step in range(s):
            if d == 'U':
                headPos[0]+=1
            elif d == 'D':
                headPos[0]-=1
            elif d == 'R':
                headPos[1]+=1
            elif d == 'L':
                headPos[1]-=1
            else:
                log(red("Unknown direction", d))

            adjustTailPos(headPos, tailPos)

            if not tailPos in tailPositions:
                tailPositions.append([]+tailPos)

    # log("head", headPos, "tail", tailPos)

    result=len(tailPositions)

    return (result,EXPECTED_RESULT)