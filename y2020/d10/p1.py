import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 2484

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)

    raw.append(0)
    raw.append(max(raw)+3)
    
    raw.sort()

    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    differences = [inputData[i+1] - inputData[i] for i in range(len(inputData)-1)]

    diff1s = diff3s = 0

    for diff in differences:
        if diff==1:
            diff1s+=1
        elif diff==3:
            diff3s+=1

    # log(diff1s, diff3s)

    result=diff1s*diff3s

    return (result, EXPECTED_RESULT)

 
