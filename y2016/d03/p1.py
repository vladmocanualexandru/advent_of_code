import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 862

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,' ')
    
    processed=[]

    for entry in raw:
        processed.append([r for r in entry if r != None])

    return processed 

def solution(inputFile):
    processed = getInputData(inputFile)

    triangleCount = 0

    for triangleCandidate in processed:
        if triangleCandidate[0]+triangleCandidate[1]>triangleCandidate[2]:
            if triangleCandidate[2]+triangleCandidate[1]>triangleCandidate[0]:
                if triangleCandidate[0]+triangleCandidate[2]>triangleCandidate[1]:
                    triangleCount+=1

    result = triangleCount
    return (result,EXPECTED_RESULT)

 