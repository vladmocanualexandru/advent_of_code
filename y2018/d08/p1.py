import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 41555

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile)
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample', inputData[:10])

    # log(inputData)

    pos = 2
    stack = []
    stack.append([inputData[0], inputData[1]])

    result=0
    while len(stack)>0 and pos<len(inputData):
        if stack[-1][0]==0:
            # log("metadata", inputData[pos:pos+stack[-1][1]])
            result+=sum(inputData[pos:pos+stack[-1][1]])
            pos+=stack[-1][1]
            stack.pop(-1)
        else:
            stack[-1][0]-=1
            stack.append([inputData[pos], inputData[pos+1]])
            pos+=2

    return (result,EXPECTED_RESULT)

 

