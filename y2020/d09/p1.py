import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 14144619

PREAMBLE_SIZE = 25

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=raw

    return processed 

def numberIsValid(candidateIndex, data):

    preamble = data[candidateIndex-PREAMBLE_SIZE:candidateIndex]
    candidate = data[candidateIndex]

    index = candidateIndex-PREAMBLE_SIZE
    while index<candidateIndex-1:
        for index2 in range(index+1, candidateIndex):
            if data[index]+data[index2] == candidate:
                return True

        index+=1

    return False

def solution(inputFile):

    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result=None

    for candidateIndex in range(PREAMBLE_SIZE,len(inputData)):
        if not numberIsValid(candidateIndex, inputData):
            result = inputData[candidateIndex]
            break

    return (result, EXPECTED_RESULT)

 
