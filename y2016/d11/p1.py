import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = None

def getInputData(inputFile):
    raw = getTuples_text(inputFile, 'contains ', 'a ', ' and ', ', ')
    
    processed=[[t2.replace('-compatible','').replace('nothing relevant','').replace('.','') for t2 in t1[1:] if not t2 == ''] for t1 in raw]

    return processed 

def solution(inputFile):
    floors = getInputData(inputFile)

    log('input', floors)

    targetCount = sum([sum(1 for item in floor if not item == '') for floor in floors])
    currentFloor = 0

    while len(floors[3])<targetCount:
        break

    result=None
    return (result,EXPECTED_RESULT)