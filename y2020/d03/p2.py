import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 3621285278

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # matrixUtils.log(inputData, '', lambda e: log(e))

    result = 1

    movementTuples = [([1,3,5,7], 1), ([1], 2)]

    for movTuple in movementTuples:
        for horizVal in movTuple[0]:
            treeCount = 0
            horizPos = horizVal

            for lineIndex in range(movTuple[1],len(inputData),movTuple[1]):
                line = inputData[lineIndex]

                if line[horizPos] == '#':
                    treeCount+=1
                horizPos = (horizPos+horizVal)%len(line)
            
            result*=treeCount

    return (result, EXPECTED_RESULT)

 
