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
 
EXPECTED_RESULT = None
WRONG_RESULTS = []

def getInputData(inputFile):
    phase1 = getTuples_numbers(inputFile, ": closest beacon is at x=", "Sensor at x=", ", y=", ", y=")
    
    phase2=[entry[1:] for entry in phase1]

    phase3=[[entry[0], entry[1], entry[2], entry[3]] for entry in phase2]

    return phase3 

def getManhattanDistance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def solution(inputFile):
    sensorReadings = getInputData(inputFile)

    # create initial list of candidates from first reading
    allPP = []
    intersectedPP = []

    for reading in sensorReadings:
        log(reading)
    # reading = sensorReadings[0]
        # add 1 to target unreachable perimeter
        mDist = getManhattanDistance(reading[0],reading[1],reading[2],reading[3]) + 1
        reading.append(mDist)
        
        # based on manhattan distance to identified beacon, generate signal out of reach perimeter
        for xy in range(mDist):
            point = (reading[0]+xy,reading[1]-mDist+xy)
            if point in allPP:
                intersectedPP.append(point)
            else:
                allPP.append(point)

            point = (reading[0]+mDist-xy,reading[1]+xy)
            if point in allPP:
                intersectedPP.append(point)
            else:
                allPP.append(point)

            point = (reading[0]-xy,reading[1]+mDist-xy)
            if point in allPP:
                intersectedPP.append(point)
            else:
                allPP.append(point)

            point = (reading[0]-mDist+xy,reading[1]-xy)
            if point in allPP:
                intersectedPP.append(point)
            else:
                allPP.append(point)

    candidates = []
    for point in intersectedPP:
        for reading in sensorReadings:
            if getManhattanDistance(point[0],point[1],reading[0],reading[1])<reading[4]:
                break
        else:
            candidates.append(point)

    log(len(candidates))

    # # iterate through all other readings
    # for reading in sensorReadings[1:]:
    #     # add 1 to target unreachable perimeter
    #     mDist = getManhattanDistance(reading[0],reading[1],reading[2],reading[3]) + 1
        
    #     newCandidates = []
    #     # same as before - generate out of reach point, but keep only if it's present in the current list of candidates
    #     for xy in range(mDist):
    #         candidate = (reading[0]+xy,reading[1]-mDist+xy)
    #         if candidate in candidates:
    #             newCandidates.append(candidate)

    #         candidate = (reading[0]+mDist-xy,reading[1]+xy)
    #         if candidate in candidates:
    #             newCandidates.append(candidate)

    #         candidate = (reading[0]-xy,reading[1]+mDist-xy)
    #         if candidate in candidates:
    #             newCandidates.append(candidate)

    #         candidate = (reading[0]-mDist+xy,reading[1]-xy)
    #         if candidate in candidates:
    #             newCandidates.append(candidate)

    #     candidates = newCandidates

    


    # cave = matrixUtils.generate(60,60,'.')
    # for reading in sensorReadings:
    #     cave[reading[1]][reading[0]] = 'S'
    #     cave[reading[3]][reading[2]] = 'B'

    # for candidate in candidates:
    #     cave[candidate[1]][candidate[0]] = 'x'

    # cave[31][34] = 'R'

    # logMatrix(cave, highlightElem=lambda e: light('R') if e == 'R' else dark(e))

    # log(candidates)
   
    result = 0

    if len(WRONG_RESULTS)>0:
        log(red("Wrong results", WRONG_RESULTS))

    return (result,EXPECTED_RESULT)