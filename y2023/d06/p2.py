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

EXPECTED_RESULT = 37286485
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, 'Time:', 'Distance:', ' ')

    times = int(''.join(raw[0]))
    distances = int(''.join(raw[1]))
    
    return ([times], [distances]) 

def solution(inputFile):
    result = 1
    
    (times, distances) = getInputData(inputFile)

    for raceId in range(len(times)):
        time = times[raceId]
        distance = distances[raceId]

        attemptCounter=0
        for attempt in range(int(time/2), 1, -1):
            if attempt*(time-attempt)<=distance:
                break
            attemptCounter+=1

        attemptCounter*=2
        
        if (time%2 == 0):
            attemptCounter-=1
        
        result*=attemptCounter

    return (result, EXPECTED_RESULT)