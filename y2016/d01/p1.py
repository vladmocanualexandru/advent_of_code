import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 253

def getInputData(inputFile):
    raw = getTuples_text(inputFile,', ')
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # input = ['R2','L3']
    # input = ['R2','R2','R2']
    # input = ['R5', 'L5', 'R5', 'R3']

    deltaValues = [0,1,0,-1]

    xDeltaIndex = 0
    yDeltaIndex = 1

    xPos = 0
    yPos = 0

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

        xPos+=deltaValues[xDeltaIndex]*value
        yPos+=deltaValues[yDeltaIndex]*value

    # log(xPos, yPos)
    result = abs(xPos)+abs(yPos)
    return (result ,EXPECTED_RESULT)

 