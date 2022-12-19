import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = '8c35d1ab'

def getInputData(inputFile):
    raw = getText(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    input = getInputData(inputFile)
    # input = 'abc'

    result = ['_' for a in range(8)]
    allowedPositions = [str(d) for d in range(8)]

    candidate = 0
    matches = 0
    while matches<8:
        hash = getMD5Hash(input, candidate)
        if hash[0:5] == '00000' and hash[5] in allowedPositions:
            position = int(hash[5])
            if result[position] == '_' :
                result[int(hash[5])] = hash[6]
                # log(''.join(result))
                matches+=1

        candidate += 1

    return (''.join(result),EXPECTED_RESULT)

 