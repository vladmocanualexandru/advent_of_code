import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1980

LIST_SIZE = 256

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input', inputData)

    elements = [i for i in range(LIST_SIZE)]
    currentPos = 0
    skipSize = 0

    for intervalSize in inputData:
        for i in range(currentPos, currentPos+round(intervalSize/2)):
            pos1 = i%LIST_SIZE
            pos2 = (2*currentPos+intervalSize-i-1)%LIST_SIZE

            (elements[pos1],elements[pos2])=(elements[pos2],elements[pos1])

        currentPos += intervalSize + skipSize
        skipSize+=1

    result=elements[0]*elements[1]
    return (result,EXPECTED_RESULT)

 

