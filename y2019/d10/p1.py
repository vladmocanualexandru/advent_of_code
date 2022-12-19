import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 326

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')
    
    processed=raw

    return processed 

def getLineEquation(p1,p2):

    dy = p2[0]-p1[0]
    dx = p2[1]-p1[1]

    return (dy,dx,dx*p1[0]-dy*p1[1])

def isPointOnLine(p, lineEq):
    return lineEq[0]*p[1]-lineEq[1]*p[0]+lineEq[2] == 0

def getDistance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def solution(inputFile):
    matrix = getInputData(inputFile)
    # matrixUtils.log(matrix, '', log)

    points = {}

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '#':
                points['%d_%d' % (y,x)] = (y,x)

    result = 0

    # counts = {}
    result = 0
    stationLocation = None
    for startPoint in points:
        asteroidCount = 0
        for endPoint in points:
            if startPoint != endPoint:
                lineEq = getLineEquation(points[startPoint], points[endPoint])

                discardEndPoint = False
                for obstaclePoint in points:
                    if not obstaclePoint in [startPoint,  endPoint]:
                        if isPointOnLine(points[obstaclePoint],lineEq) and (max(getDistance(points[obstaclePoint], points[startPoint]),getDistance(points[obstaclePoint], points[endPoint]))<getDistance(points[startPoint], points[endPoint])):
                            discardEndPoint = True
                            break
                
                if not discardEndPoint:
                    asteroidCount+=1

        # counts[startPoint] = asteroidCount
        if asteroidCount>result:
            result = asteroidCount
            stationLocation = startPoint

    # log("station location", stationLocation)

    return (result,EXPECTED_RESULT)

 

