import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 2081

def getInputData(inputFile):
    raw = getRawText(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    inputData = getRawText(inputFile)
    # inputData = '^v^v^v^v^v'

    currentPosition = [0,0]
    positionSet = {'0x0'}

    for command in inputData:
        if command == '^':
            currentPosition[1]+=1
        elif command == '>':
            currentPosition[0]+=1
        elif command == 'v':
            currentPosition[1]-=1
        else:
            currentPosition[0]-=1

        positionSet.add('%sx%s' % (currentPosition[0],currentPosition[1]))

    result = len(positionSet)
    
    return (result, EXPECTED_RESULT)

 