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

EXPECTED_RESULT = 1304

LIMIT = 150
 
def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=[entry for entry in raw]

    return processed 

def chooseContainer(i, containers, currentVolume, currentSollution, sollutionCollector):
    # log(currentSollution, " - ", i)
    if currentVolume + containers[i] == LIMIT:
        sollutionCollector.append(currentSollution+[containers[i]])
    elif currentVolume + containers[i] < LIMIT:
        currentVolume+=containers[i]
        
        for j in range(i+1, len(containers), 1):
            chooseContainer(j, containers, currentVolume, currentSollution+[containers[i]], sollutionCollector)

def solution(inputFile):
    containers = getInputData(inputFile)
    containers.sort()

    sollutionCollector = []
    for i in range(len(containers)):
        chooseContainer(i, containers, 0, [], sollutionCollector)

    # log(sollutionCollector)

    result = len(sollutionCollector)
    return (result, EXPECTED_RESULT)