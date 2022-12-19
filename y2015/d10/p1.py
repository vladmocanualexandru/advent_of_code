import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 492982

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'')
    
    processed=raw[0]

    return processed 

STEPS = 40

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample (first 20)', inputData[:20])

    for step in range(STEPS):
        result = []
        i = 0
        while i < len(inputData):
            count = 1
            for j in range(i+1, len(inputData)+1):
                if j==len(inputData) or inputData[i]!=inputData[j]:
                    result.append(count)
                    result.append(inputData[i])
                    i = j
                    break
                else:
                    count+=1

        inputData = result

    return (len(result), EXPECTED_RESULT)

 

