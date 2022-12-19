import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 2341

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'x')
    
    processed=raw

    return processed

def solution(inputFile):
    inputData = getRawText(inputFile)
    # input = '^v^v^v^v^v'

    santaPosition = [0,0]
    roboSantaPosition = [0,0]

    positionSet = {'0x0'}

    santaMovesNow=True
    for command in inputData:
        santaMove = 0
        roboSantaMove = 1

        if santaMovesNow:
            santaMove = 1
            roboSantaMove = 0

        if command == '^':
            santaPosition[1]+=santaMove
            roboSantaPosition[1]+=roboSantaMove
        elif command == '>':
            santaPosition[0]+=santaMove
            roboSantaPosition[0]+=roboSantaMove
        elif command == 'v':
            santaPosition[1]-=santaMove
            roboSantaPosition[1]-=roboSantaMove
        else:
            santaPosition[0]-=santaMove
            roboSantaPosition[0]-=roboSantaMove

        positionSet.add('%sx%s' % (santaPosition[0],santaPosition[1]))
        positionSet.add('%sx%s' % (roboSantaPosition[0],roboSantaPosition[1]))

        santaMovesNow = not santaMovesNow

    result = len(positionSet)

    return (result, EXPECTED_RESULT)
 