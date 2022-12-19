import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=[r for r in raw]

    return processed 


def solution(inputFile):
    input = getInputData(inputFile)
    threeSums = []

    for index in range(len(input)):
        if  (index+2)>=len(input):
            break

        threeSums.append(input[index]+input[index+1]+input[index+2])

    result = 0

    for index in range(len(threeSums)-1):
        if threeSums[index+1]>threeSums[index]:
            result = result + 1

    return (result,1150)