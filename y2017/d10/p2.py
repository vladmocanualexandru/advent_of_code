import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = '899124dac21012ebc32e2f4d11eaec55'

LIST_SIZE = 256
ROUND_COUNT = 64

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[ord(c) for c in raw[0]]

    processed += [17, 31, 73, 47, 23]

    return processed 

def xorArray(arr):
    result = arr[0]
    for e in arr[1:]:
        result ^= e

    return result

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input', inputData)

    elements = [i for i in range(LIST_SIZE)]
    currentPos = 0
    skipSize = 0

    for r in range(ROUND_COUNT):
        for intervalSize in inputData:
            for i in range(currentPos, currentPos+round(intervalSize/2)):
                pos1 = i%LIST_SIZE
                pos2 = (2*currentPos+intervalSize-i-1)%LIST_SIZE

                (elements[pos1],elements[pos2])=(elements[pos2],elements[pos1])

            currentPos += intervalSize + skipSize
            skipSize+=1

    elementsHex = []
    for i in range(16):
        elementsHex.append(hex(xorArray(elements[i*16:(i+1)*16]))[2:])

    # log(elementsHex)

    result=''.join([e if len(e) == 2 else ('0%s' % e) for e in elementsHex])
    return (result,EXPECTED_RESULT)

 

