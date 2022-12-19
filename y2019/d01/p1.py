import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 3323874

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    return raw


def solution(inputFile):
    inputData = getInputData(inputFile)

    return (sum([(math.floor(m/3)-2) for m in inputData]), EXPECTED_RESULT)

 
