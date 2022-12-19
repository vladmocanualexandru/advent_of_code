import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 61529

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    input = getInputData(inputFile)
    # input = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

    keypad = [[7,8,9],[4,5,6],[1,2,3]]
    posX = posY = 1

    result = 0

    for instruction in input:
        for command in instruction:
            if command == 'U':
                posY = min(posY+1, 2)
            elif command == 'D':
                posY = max(posY-1, 0)
            elif command == 'L':
                posX = max(posX-1, 0)
            else:
                posX = min(posX+1, 2)
            
        result = result*10+keypad[posY][posX]

    return (result,EXPECTED_RESULT)

 