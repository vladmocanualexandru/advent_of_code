import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 126

def getInputData(inputFile):
    raw = getTuples_text(inputFile,', ')
    
    processed=raw[0]

    return processed 

def generatePath(x,y,xDelta,yDelta, steps):
    result = []
    for i in range(steps):
        x+=xDelta
        y+=yDelta
        result.append('%s_%s'%(y,x))
        
    return result

def solution(inputFile):
    inputData = getInputData(inputFile)
    # input = ['R2','L3']
    # input = ['R2','R2','R2']
    # input = ['R5', 'L5', 'R5', 'R3']
    # input = ['R8','R4','R4','R8']

    deltaValues = [0,1,0,-1]

    xDeltaIndex = 0
    yDeltaIndex = 1

    xPos = 0
    yPos = 0

    pathNodes = []

    result = None
    for instruction in inputData:
        command = instruction[0]
        value = int(instruction[1:])

        if command == 'R':
            xDeltaIndex=(xDeltaIndex+1)%4
            yDeltaIndex=(yDeltaIndex+1)%4
        else:
            if xDeltaIndex == 0:
                xDeltaIndex = 3
            else:
                xDeltaIndex-=1

            if yDeltaIndex == 0:
                yDeltaIndex = 3
            else:
                yDeltaIndex-=1

        for node in generatePath(xPos,yPos,deltaValues[xDeltaIndex], deltaValues[yDeltaIndex], value):
            if node in pathNodes:
                # log(node)

                result = sum([int(tkn) for tkn in node.split('_')])
                return (result,EXPECTED_RESULT)
               
            pathNodes.append(node)

        xPos+=deltaValues[xDeltaIndex]*value
        yPos+=deltaValues[yDeltaIndex]*value
  
 