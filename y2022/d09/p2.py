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
 
EXPECTED_RESULT = 2259

LINKS = 8

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')
    
    processed=[(entry[0],int(entry[1])) for entry in raw]

    return processed 

def adjustTailPos(headPos, tailPos):
    yDif = abs(headPos[0]-tailPos[0])
    xDif = abs(headPos[1]-tailPos[1])
    if yDif == xDif == 2:
        tailPos[0] = int((headPos[0]+tailPos[0])/2)
        tailPos[1] = int((headPos[1]+tailPos[1])/2)
    elif yDif == 2:
        tailPos[1] = headPos[1]
        tailPos[0] = int((headPos[0]+tailPos[0])/2)
    elif xDif == 2:
        tailPos[0] = headPos[0]
        tailPos[1] = int((headPos[1]+tailPos[1])/2)

def solution(inputFile):
    moves = getInputData(inputFile)

    headPos = [0,0]
    links = [[0,0] for i in range(LINKS)]
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

            adjustTailPos(headPos, links[0])
            
            for linkIndex in range(1,len(links)):
                adjustTailPos(links[linkIndex-1], links[linkIndex])


            adjustTailPos(links[-1], tailPos)

            if not tailPos in tailPositions:
                tailPositions.append([]+tailPos)
        
        # m = matrixUtils.generate(60,60,'.')

        # m[tailPos[0]+30][tailPos[1]+30] = 'T'
        # for linkIndex in range(len(links)-1,-1,-1):
        #     m[links[linkIndex][0]+30][links[linkIndex][1]+30] = linkIndex+1
        # m[headPos[0]+30][headPos[1]+30] = 'H'

        # matrixUtils.log(matrixUtils.flipVertical(m), '', log)
        # log('')


    # log("head", headPos, "tail", tailPos)

    result=len(tailPositions)

    return (result,EXPECTED_RESULT)