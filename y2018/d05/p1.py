import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 11720

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # # log('sample', inputData[:10])

    targets = [ '%s%s' % (c, c.upper()) for c in list(string.ascii_lowercase)]
    targets += [t[::-1] for t in targets]

    while True:
        currentLen = len(inputData)
        for target in targets:
            inputData = inputData.replace(target, '')
        
        if len(inputData) == currentLen:
            break

    result=len(inputData)
    return (result,EXPECTED_RESULT)

 
