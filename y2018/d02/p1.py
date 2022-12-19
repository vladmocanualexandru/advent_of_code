from itertools import count
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 5880

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def countChars(text):
    counts = {}
    for c in text:
        if not c in counts:
            counts[c] = 1
        else:
            counts[c] +=1

    justCounts = []
    for c in counts:
        justCounts.append(counts[c])

    return justCounts

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    doubleCounts = 0
    tripleCounts = 0

    for text in inputData:
        counts = countChars(text)

        if 2 in counts:
            doubleCounts+=1

        if 3 in counts:
            tripleCounts+=1
        
    result=doubleCounts*tripleCounts

    return (result,EXPECTED_RESULT)

 
