import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile="input.txt"):
    raw = getTuples_text(inputFile)

    data = []
    for entry in raw:
        tkns1 = entry[1].split(',')
        
        tknsX = tkns1[0].split('..')
        tknsY = tkns1[1].split('..')
        tknsZ = tkns1[2].split('..')

        x1 = int(tknsX[0][2:])+50
        x2 = int(tknsX[1])+50
        y1 = int(tknsY[0][2:])+50
        y2 = int(tknsY[1])+50
        z1 = int(tknsZ[0][2:])+50
        z2 = int(tknsZ[1])+50

        if x1>=0 and x2<=100 and y1>=0 and y2<=100 and z1>=0 and z2<=100:
            data.append((entry[0],x1,x2,y1,y2,z1,z2))

    return data


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log(inputData)

    matrix = []
    
    for i in range(101):
        matrix.append(matrixUtils.generate(101,101,-1))

    for step in inputData:
        for y in range(step[3], step[4]+1, 1):
            for x in range(step[1], step[2]+1, 1):
                for z in range(step[5], step[6]+1, 1):

                    matrix[y][x][z] = -1 if step[0] == 'off' else matrix[y][x][z]+1

    # VIZUALIZATION
    availableColorCodes = [31,32,33,34,35,36]
    vizMatrix = matrixUtils.generate(101,101,0)
    for line in range(101):
        for col in range(101):
            vizMatrix[line][col] = max(matrix[line][col])

    vizMatrix = matrixUtils.wrap(vizMatrix,-1,5)

    # matrixUtils.log(vizMatrix, '', log, lambda e: ' ' if e == -1 else formatOutput(availableColorCodes[(e+1)%6],C_BLOCK))

    # VIZUALIZATION OFF

    result = 0
    for layer in matrix:
        result += matrixUtils.addAll(layer, lambda e: e>-1, lambda e: 1)

    return (result,596989)