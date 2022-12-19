import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1034

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'')
    return raw


def solution(inputFile):
    inputData = getInputData(inputFile)[0]

    result=sum([inputData[i] for i in range(len(inputData)) if inputData[i]==inputData[(i+1)%len(inputData)]])



    # log(inputData)


    return (result,EXPECTED_RESULT)

 
