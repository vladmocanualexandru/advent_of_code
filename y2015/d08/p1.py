import sys, os, re

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1333

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):

    inputData = getInputData(inputFile)

    numberChars=0
    numberCharsMem=0
    for line in inputData:
        parsed = re.sub('\\\\x..','_',line[1:-1].replace('\\"','_').replace('\\\\','_'))

        # log(line, len(line))
        # log(parsed, len(parsed))

        numberChars += len(line)
        numberCharsMem += len(parsed)

    # log(numberChars, numberCharsMem)

    result = numberChars - numberCharsMem

    return (result, EXPECTED_RESULT)

 