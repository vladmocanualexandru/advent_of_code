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

LIMIT = 150
 
def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=[entry for entry in raw]

    return processed 

def chooseContainer(i, containers, currentVolume, currentSollution, sollutionCollector):
    if currentVolume + containers[i] == LIMIT:
        sollutionCollector.append(currentSollution+1)
    elif currentVolume + containers[i] < LIMIT:
        currentVolume+=containers[i]
        
        for j in range(i+1, len(containers), 1):
            chooseContainer(j, containers, currentVolume, currentSollution+1, sollutionCollector)

def solution(inputFile):
    containers = getInputData(inputFile)
    containers.sort()

    sollutionCollector = []
    for i in range(len(containers)):
        chooseContainer(i, containers, 0, 0, sollutionCollector)

    solColS = pd.Series(sollutionCollector)

    # log(solColS.value_counts(dropna=False)[np.min(solColS)])

    result = solColS.value_counts(dropna=False)[np.min(solColS)]
    return (result, EXPECTED_RESULT)