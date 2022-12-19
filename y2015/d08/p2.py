import sys, os, re

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 2046

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)

    numberChars=0
    numberCharsEncoded=0
    for line in inputData:
        # parsed = re.sub('\\\\x..','_',line[1:-1].replace('\\"','_').replace('\\\\','_'))
        parsed = '"%s"' % line.replace('\\','\\\\').replace('"','\\"')

        # log(line, len(line))
        # log(parsed, len(parsed))

        numberChars += len(line)
        numberCharsEncoded += len(parsed)

    # log(numberChars, numberCharsEncoded)

    result = numberCharsEncoded - numberChars

    return (result, EXPECTED_RESULT)

 