import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 'cyrupz'

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' (', ')', ' -> ', ', ')
    
    processed=[(t[0], t[3:]) for t in raw]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample', inputData[:10])

    children = []
    for entry in inputData:
        children += entry[1]
    
    result=None
    for entry in inputData:
        if not entry[0] in children:
            result = entry[0]
            break

    return (result,EXPECTED_RESULT)

 

