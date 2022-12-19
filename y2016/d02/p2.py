import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 'C2C28'

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    input = getInputData(inputFile)
    # input = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

    keypad = [
        ['.','.','.','.','.','.','.'],
        ['.','.','.','D','.','.','.'],
        ['.','.','A','B','C','.','.'],
        ['.','5','6','7','8','9','.'],
        ['.','.','2','3','4','.','.'],
        ['.','.','.','1','.','.','.'],
        ['.','.','.','.','.','.','.']
    ]

    posX = 1 
    posY = 3

    result = ''

    for instruction in input:
        for command in instruction:
            posXCandidate = posX
            posYCandidate = posY
            if command == 'U':
                posYCandidate = posY+1
            elif command == 'D':
                posYCandidate = posY-1
            elif command == 'L':
                posXCandidate = posX-1
            else:
                posXCandidate = posX+1

            if keypad[posYCandidate][posXCandidate]!='.':
                posX = posXCandidate
                posY = posYCandidate
            
        result += keypad[posY][posX]

    return (result,EXPECTED_RESULT)

 