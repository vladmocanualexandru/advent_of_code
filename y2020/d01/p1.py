import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 751776

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    return raw


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log(inputData)

    # combos = [(inputData[i],inputData[j]) for i in range(0, len(inputData)-1) for j in range(i+1, len(inputData)) if inputData[i]+input[j]==2020]

    for i in range(len(inputData)-1):
        for j in range(i+1, len(inputData)):
            if inputData[i]+inputData[j]==2020:
                return (inputData[i]*inputData[j],EXPECTED_RESULT)

 
