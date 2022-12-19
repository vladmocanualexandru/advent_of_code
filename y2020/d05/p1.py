import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 911

def replaceLetters(text):
    return text.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=[replaceLetters(r) for r in raw]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[0])

    result=-1

    for entry in inputData:
        id = int('0b'+entry[:7], 2) * 8 + int('0b'+entry[7:], 2)
        result = max(result, id) 

    return (result, EXPECTED_RESULT)

 
