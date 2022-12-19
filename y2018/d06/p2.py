import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 36136

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')

    minX = maxX = raw[0][0]
    minY = maxY = raw[0][1]

    for r in raw:
        minX = min(minX, r[0])
        minY = min(minY, r[1])
        maxX = max(maxX, r[0])
        maxY = max(maxY, r[1])

    processed=[(r[1]-minY, r[0]-minX) for r in raw]

    return (processed, maxY-minY+1, maxX-minX+1 ) 

def calculateDistanceSum(y, x, points):
    result = sum([abs(y-points[p][0])+abs(x-points[p][1]) for p in points])

    return result

def solution(inputFile):
    inputData = getInputData(inputFile)
    # # log('input', inputData)

    matrix = matrixUtils.generate(inputData[1], inputData[2], -1)
    labels = ['%s0' % l for l in list(string.ascii_uppercase)]+['%s1' % l for l in list(string.ascii_uppercase)]+['%s2' % l for l in list(string.ascii_uppercase)]

    wrapSize = 0

    points = {}
    for i in range(len(inputData[0])):
        coord = inputData[0][i]
        matrix[coord[0]][coord[1]] = labels[i]
        points[labels[i]] = (coord[0]+wrapSize,coord[1]+wrapSize)

    # matrix = matrixUtils.wrap(matrix, -1, wrapSize)

    # log(points)
    # matrixUtils.log(matrix,', ',log)

    for lineI in range(len(matrix)):
        for colI in range(len(matrix[0])):
            matrix[lineI][colI] = calculateDistanceSum(lineI, colI, points)

    threshold = 10000
    # matrixUtils.log(matrix,', ',log)
    # matrixUtils.log(matrix,'',log,lambda e: purple(C_BLOCK) if e<threshold else '.')
 
    result = matrixUtils.addAll(matrix, lambda e: e<threshold, lambda e: 1)
    return (result,EXPECTED_RESULT)

 
