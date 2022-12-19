from itertools import combinations
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 2765

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'	')
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input', inputData)
    
    result=0
    combinations = []

    combination = str(inputData)
    loopCombination = None

    scenario1 = True
    scenario2 = True
    while (scenario1 and not combination in combinations) or (scenario2 and combination != loopCombination):

        if scenario1:
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
        result += 1
        if scenario1 and combination in combinations:
            # log('Found loop combination!')
            scenario1 = False
            scenario2 = True

            loopCombination = combination
            combination = None
            result = 0

    return (result,EXPECTED_RESULT)

 

