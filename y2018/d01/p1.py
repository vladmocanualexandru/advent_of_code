import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 585

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    return raw

def solution(inputFile):
    result= sum(getInputData(inputFile))

    return (result,EXPECTED_RESULT)

 
