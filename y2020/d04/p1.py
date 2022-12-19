import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 170

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)
    # # log('sample', inputData)

    result=0

    fieldsToCheck = [
        'byr:',
        'iyr:',
        'eyr:',
        'hgt:',
        'hcl:',
        'ecl:',
        'pid:'
    ]

    outcome = [False for f in fieldsToCheck]

    for line in inputData:
        if line == '':
            if not False in outcome:
                result+=1

            outcome = [False for f in fieldsToCheck]
        else:
            for checkIndex in range(len(outcome)):
                if not outcome[checkIndex]:
                    if fieldsToCheck[checkIndex] in line:
                        outcome[checkIndex] = True

    # last lines represent last passport
    if not False in outcome:
        result+=1

    return (result, EXPECTED_RESULT)

 
