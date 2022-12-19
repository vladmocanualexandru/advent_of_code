import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1577

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,' ')
    
    processed=[]
    for entry in raw:
        processed.append([r for r in entry if r != None])

    return processed 

def solution(inputFile):
    processed = getInputData(inputFile)

    triangles = []

    for i in range(0, len(processed), 3):
        for j in range(3):
            triangles.append([processed[i][j],processed[i+1][j],processed[i+2][j]])

    triangleCount = 0

    for triangleCandidate in triangles:
        if triangleCandidate[0]+triangleCandidate[1]>triangleCandidate[2]:
            if triangleCandidate[2]+triangleCandidate[1]>triangleCandidate[0]:
                if triangleCandidate[0]+triangleCandidate[2]>triangleCandidate[1]:
                    triangleCount+=1

    result = triangleCount
    return (result,EXPECTED_RESULT)

 

