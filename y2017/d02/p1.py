import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 21845

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result=0
    for tuple in inputData:
        result += max(tuple) - min(tuple)

    return (result,EXPECTED_RESULT)

 
