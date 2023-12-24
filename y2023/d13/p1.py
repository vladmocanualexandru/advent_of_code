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

EXPECTED_RESULT = 34993
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=[]

    pattern = []
    for line in raw:
        if line == ['']:
            processed.append([]+pattern)
            pattern = []
        else:
            pattern.append(line[0])

    processed.append([]+pattern)
    
    return processed 

def checkColumn(pattern, colIndex):
    for lineIndex in range(len(pattern)):
        offset = 1
        while colIndex+1-offset >=0 and colIndex+offset < len(pattern[0]):
            if pattern[lineIndex][colIndex+1-offset]!=pattern[lineIndex][colIndex+offset]:
                return False
            offset+=1
    return True

def findVerticalSimmetry(pattern):
    for colIndex in range(len(pattern[0])-1):
        if checkColumn(pattern, colIndex):
            return colIndex

    return -1

def checkLine(pattern, lineIndex):
    for colIndex in range(len(pattern[0])):
        offset = 1
        while lineIndex+1-offset >=0 and lineIndex+offset < len(pattern):
            if pattern[lineIndex+1-offset][colIndex]!=pattern[lineIndex+offset][colIndex]:
                return False
            offset+=1
    return True

def findHorizontalSimmetry(pattern):
    for lineIndex in range(len(pattern)-1):
        if checkLine(pattern, lineIndex):
            return lineIndex

    return -1
        


def solution(inputFile):
    result = 0
    
    inputData = getInputData(inputFile)
    for pattern in inputData:
        v = findVerticalSimmetry(pattern)
        h = findHorizontalSimmetry(pattern)
        
        result += (v+1 if v>-1 else 0) + ((h+1)*100 if h>-1 else 0)

    # log(red())
    return (result, EXPECTED_RESULT)