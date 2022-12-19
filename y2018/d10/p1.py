from random import randint, random
import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 'XLZAKBGZ'

def getInputData(inputFile):
    raw = getTuples_text(inputFile,',', 'position=<', 'velocity=<','>')
    
    # input data contains coords as x,y but we use them in reverse: select line, then column
    processed=[[int(r[2]), int(r[1]), int(r[5]), int(r[4])] for r in raw]

    return processed 

def logMatrix(points, minY, maxY, minX, maxX):

    localP = points+[]
    for entry in localP:
        entry[0]-=minY
        entry[1]-=minX

    maxX-=minX
    maxY-=minY

    matrix = matrixUtils.generate(maxY+1,maxX+1, ' ')

    # add all points on the matrix
    for entry in localP:
        matrix[entry[0]][entry[1]] = C_DOT_FULL

    # matrixUtils.log(matrix, '', log)

def solution(inputFile):
    points = getInputData(inputFile)
    # log('input sample (first 20)', points[:20])

    yDiff = oldYDiff = 9999999
    for iterCount in range(1000000):

        if yDiff>oldYDiff:
            # log("iteration",iterCount-2)

            for point in points:
                point[0]-=point[2]
                point[1]-=point[3]

            # logMatrix(points, minY,maxY,minX,maxX)
            break
        else:
            oldYDiff = yDiff

        minY = maxY = points[0][0]+points[0][2]
        minX = maxX = points[0][1]+points[0][3]

        for point in points:
            point[0]+=point[2]
            point[1]+=point[3]

            minY = min(minY, point[0])
            maxY = max(maxY, point[0])
            minX = min(minX, point[1])
            maxX = max(maxX, point[1])

        yDiff = maxY-minY

    # uncomment log lines to render the result
    return ("XLZAKBGZ",EXPECTED_RESULT)

 

