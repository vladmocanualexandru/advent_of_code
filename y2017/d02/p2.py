import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 191

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result=0
    for tuple in inputData:
        nextTuple = False
        for i in range(len(tuple)-1):
            for j in range(i+1, len(tuple)):
                div = 1.0*max(tuple[i], tuple[j])/min(tuple[i], tuple[j])
                if div == math.floor(div):
                    nextTuple = True
                    result += div
                    break

            if nextTuple:
                break

    return (int(result),EXPECTED_RESULT)

 
