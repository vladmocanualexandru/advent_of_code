import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 13743542639657
WRONG_RESULTS = []

TARGET_MIN = 0
TARGET_MAX = 4000000

def getInputData(inputFile):
    phase1 = getTuples_numbers(inputFile, ": closest beacon is at x=", "Sensor at x=", ", y=", ", y=")
    
    phase2=[entry[1:] for entry in phase1]

    phase3=[[entry[0], entry[1], entry[2], entry[3]] for entry in phase2]

    return phase3 



def solution(inputFile):
    sensorReadings = getInputData(inputFile)

    # create initial list of candidates from first reading

    perimeterSides = []
    for reading in sensorReadings:
        mDist = geometryUtils.getManhattanDistance(reading[0],reading[1],reading[2],reading[3])+1
        reading.append(mDist)

        (x,y) = (reading[0],reading[1])

        perimeterSides.append(((x,y+mDist),(x+mDist-1, y+1)))
        perimeterSides.append(((x+mDist, y),(x+1, y-mDist+1)))
        perimeterSides.append(((x, y-mDist),(x-mDist+1, y-1)))
        perimeterSides.append(((x-mDist, y),(x-1,y+mDist-1)))

    # log(perimeterSides)

    intersectionPoints = []
    for perimeterIndex1 in range(len(perimeterSides)-1):
        for perimeterIndex2 in range(perimeterIndex1+1,len(perimeterSides)):
            (a,b) = perimeterSides[perimeterIndex1]
            (c,d) = perimeterSides[perimeterIndex2]
            intersectionPoint = geometryUtils.getIntersection(a,b,c,d)

            if intersectionPoint != None and not intersectionPoint in intersectionPoints:
                intersectionPoints.append(intersectionPoint)

    candidates = []
    for (ipX,ipY) in intersectionPoints:
        for (sX,sY,bX,bY,mDist) in sensorReadings:
            if getManhattanDistance(ipX,ipY,sX,sY)<mDist:
                break
        else:
            if TARGET_MIN<=ipX<=TARGET_MAX and TARGET_MIN<=ipY<=TARGET_MAX:
                candidates.append((ipX,ipY))

    result = int(candidates[0][0]*4000000+candidates[0][1])

    if len(WRONG_RESULTS)>0:
        log(red("Wrong results", WRONG_RESULTS))

    return (result,EXPECTED_RESULT)