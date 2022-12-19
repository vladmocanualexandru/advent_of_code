from itertools import combinations
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 14029

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'	')
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample', inputData[:10])
    
    result=0
    combinations = []

    combination = str(inputData)
    while not combination in combinations:
        combinations.append(combination)

        maxIndex = 0
        maxValue = inputData[0]

        for index in range(1, len(inputData)):
            if inputData[index]>maxValue:
                maxValue = inputData[index]
                maxIndex = index

        inputData[maxIndex] = 0
        while maxValue>0:
            maxIndex=(maxIndex+1)%len(inputData)
            inputData[maxIndex] += 1
            maxValue-=1

        combination = str(inputData)
        result+=1

    return (result,EXPECTED_RESULT)

 

