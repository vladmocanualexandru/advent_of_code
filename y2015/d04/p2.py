import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 3938038

def getInputData(inputFile):
    raw = getText(inputFile)
    
    processed=raw

    return processed 

def hashFound(hash):
    try:
        return int(hash[0:6]) == 0
    except ValueError:
        return False


def solution(inputFile):
    # input = 'abcdef'
    # input = 'pqrstuv'
    inputData = getInputData(inputFile)

    candidate = 117946
    found = False
    while not found:
        hash = getMD5Hash(inputData, candidate)

        if hashFound(hash) or candidate == 10000000:
            break
        else:
            candidate += 1

    result = candidate

    return (result, EXPECTED_RESULT)

 