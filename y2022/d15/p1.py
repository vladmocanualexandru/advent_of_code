import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 4748135
WRONG_RESULTS = [4002875]

SCAN_Y = 2000000
PADDING = 1000010

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, ": closest beacon is at x=", "Sensor at x=", ", y=", ", y=")
    
    processed=[entry[1:] for entry in raw]

    return processed 

def getManhattanDistance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def solution(inputFile):
    sensorReadings = getInputData(inputFile)

    minX = maxX = sensorReadings[0][0]
    # minY = maxY = sensorReadings[0][1]

    for reading in sensorReadings:
        minX = min(minX, reading[0], reading[2])
        maxX = max(maxX, reading[0], reading[2])
        # minY = min(minY, reading[1], reading[3])
        # maxY = max(maxY, reading[1], reading[3])
        reading.append(getManhattanDistance(reading[0],reading[1],reading[2],reading[3]))

    # log("X interval", minX, maxX)

    result = 0

    for scanX in range(minX-PADDING, maxX+PADDING):
        for reading in sensorReadings:
            if not(scanX == reading[0] and SCAN_Y == reading[1]) and not(scanX == reading[2] and SCAN_Y == reading[3]) and getManhattanDistance(scanX, SCAN_Y, reading[0],reading[1])<=reading[4]:
                result += 1
                # log(scanX, "close to", reading)
                break

    if len(WRONG_RESULTS)>0:
        log(red("Wrong results", WRONG_RESULTS))

    return (result,EXPECTED_RESULT)