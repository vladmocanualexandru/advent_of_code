import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 6291

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[0])

    result=0

    questions = {}
    for line in inputData:
        if line == '':
            result += len(questions)
            questions = {}
        else:
            for c in line:
                questions[c] = True

    # add last group's answers
    result += len(questions)

    return (result, EXPECTED_RESULT)

 
