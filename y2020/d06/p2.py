import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 3052

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[0])

    result=0

    questions = {}
    personCount = 0
    for line in inputData:
        if line == '':
            result += sum([1 for q in questions if questions[q] == personCount])
            questions = {}
            personCount = 0
        else:
            personCount += 1
            for c in line:
                if not c in questions:
                    questions[c] = 0
                questions[c] += 1
            

    # add last group's answers
    result += sum([1 for q in questions if questions[q] == personCount])

    return (result, EXPECTED_RESULT)

 
