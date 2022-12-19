
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 'c6697b55'

def getInputData(inputFile):
    raw = getText(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    input = getInputData(inputFile)
    # input = 'abc'

    result = ''

    candidate = 0
    while len(result)<8:
        hash = getMD5Hash(input, candidate)
        if hash[0:5] == '00000':
            # log(result)
            result = result+hash[5]

        candidate += 1

    return (result,EXPECTED_RESULT)

 