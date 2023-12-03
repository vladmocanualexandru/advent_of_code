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

EXPECTED_RESULT = 56580

def buildCubesObj(config):
    obj = {"red":0, "green":0, "blue":0}

    for entry in config:
        [val, color] = entry.strip().split(" ")
        obj[color]+=int(val)

    return obj
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile,": ", ";")
    
    processed=[[buildCubesObj(elem.split(", ")) for elem in entry[1:]] for entry in raw]

    return processed 

THRESHOLD_RED = 12
THRESHOLD_GREEN = 13
THRESHOLD_BLUE = 14

def solution(inputFile):
    inputData = getInputData(inputFile)

    # log(inputData)

    result = 0

    for gameIndex in range(len(inputData)):
        maxRed = maxGreen = maxBlue = 0
        
        for pull in inputData[gameIndex]:
            maxRed = max(maxRed, pull["red"])
            maxGreen = max(maxGreen, pull["green"])
            maxBlue = max(maxBlue, pull["blue"])

        result += maxRed*maxGreen*maxBlue

    return (result, EXPECTED_RESULT)