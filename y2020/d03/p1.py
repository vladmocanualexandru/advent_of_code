import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 299

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # matrixUtils.log(inputData, '', lambda e: log(e))

    treeCount = 0
    horizPos = 3

    for line in inputData[1:]:
        if line[horizPos] == '#':
            treeCount+=1
        horizPos = (horizPos+3)%len(line)

    return (treeCount,EXPECTED_RESULT)

 
