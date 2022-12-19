import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1411

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'-')
    
    processed=raw[0]

    return processed 

def checkDigitsIncresing(candidateStr):

    for i in range(len(candidateStr)-1):
        if candidateStr[i]>candidateStr[i+1]:
            return False

    return True

def checkCharCount(candidateStr):
    counts = [0 for i in range(1,10)]

    for c in candidateStr:
        counts[int(c)-1]+=1

    return 2 in counts


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result = 0 
    for candidate in range(inputData[0], inputData[1]+1):
        candidateStr = str(candidate)
        if checkDigitsIncresing(candidateStr) and checkCharCount(candidateStr):
            result+=1

    return (result,EXPECTED_RESULT)

 
