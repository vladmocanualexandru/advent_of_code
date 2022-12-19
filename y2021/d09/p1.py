import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[]
    for line in raw:
        processed.append([int(c) for c in line])

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)

    result = 0
    for lineIndex in range(len(input)):
        for colIndex in range(len(input[lineIndex])):
            value = input[lineIndex][colIndex]

            minNeighValue = 10
            
            if lineIndex>0:
                minNeighValue = min(minNeighValue,input[lineIndex-1][colIndex])
            if colIndex>0:
                minNeighValue = min(minNeighValue,input[lineIndex][colIndex-1])
            if lineIndex<len(input)-1:
                minNeighValue = min(minNeighValue,input[lineIndex+1][colIndex])
            if colIndex<len(input[lineIndex])-1:
                minNeighValue = min(minNeighValue,input[lineIndex][colIndex+1])
            
            if value < minNeighValue:
                # log(value)
                result += 1+value

    return (result,558)