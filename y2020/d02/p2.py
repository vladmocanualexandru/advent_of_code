import sys, os, re

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 472

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ': ')

    processed = []
    for tuple in raw:
        policy = tuple[0].split(' ')
        processed.append(([int(a) for a in policy[0].split('-')], policy[1], tuple[1]))

    return processed


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[0])

    count = 0

    for entry in inputData:
        pattern = entry[1]
        text = entry[2]

        localCount = 0

        if text[entry[0][0]-1] == pattern:
            localCount+=1

        if text[entry[0][1]-1] == pattern:
            localCount+=1

        if localCount == 1:
            count+=1

    return (count,EXPECTED_RESULT)

 
