import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 330785

def getInputData(inputFile):
    raw = getRawLines(inputFile)
    
    processed=int(raw[0])

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)

    currentPos = [1,1]
    origin = [1,1]
    currentValue = 1
    matrix = matrixUtils.generate(3,3,0)
    matrix[1][1] = 1
    deltaX = 1
    deltaY = 0

    while currentValue <= inputData:

        if currentPos[0] == len(matrix)-1 and currentPos[1] == len(matrix[0])-1:
            matrix = matrixUtils.wrap(matrix, 0)
            currentPos[0]+=1
            currentPos[1]+=1
            origin[0]+=1
            origin[1]+=1
            deltaX = 1
            deltaY = 0

        currentValue = matrix[currentPos[0]][currentPos[1]] = max(1,sum(matrixUtils.getNeighbors8(matrix,currentPos[0],currentPos[1])))

        if currentPos[1] == len(matrix)-1:
            deltaX = 0
            deltaY = -1

        if currentPos[0]==0:
            deltaX = -1
            deltaY = 0

        if currentPos[1]==0: 
            deltaX = 0
            deltaY = 1

        if currentPos[0]==len(matrix)-1: 
            deltaX = 1
            deltaY = 0

        currentPos[0]+=deltaY
        currentPos[1]+=deltaX

    # matrixUtils.log(matrix, ' ', log)

    result = matrix[currentPos[0]-deltaY][currentPos[1]-deltaX]
    return (result,EXPECTED_RESULT)

 
