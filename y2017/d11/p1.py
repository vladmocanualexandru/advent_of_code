import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 720

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    # log('input sample (first 20)', inputData[:20])

    # n -> y-1
    # ne -> y-1, x+1
    # se -> x+1
    # s -> y+1
    # sw -> y+1, x-1
    # nw -> x-1

    targetX = 0
    targetY = 0

    for command in inputData:
        if command == 'n':
            targetY-=1
        elif command == 'ne':
            targetY-=1
            targetX+=1
        elif command == 'se':
            targetX+=1
        elif command == 's':
            targetY+=1
        elif command == 'sw':
            targetY+=1
            targetX-=1
        elif command == 'nw':
            targetX-=1
        else:
            log(red("unknown command "+command))

    # got lucky here - target is to the NW (squaregrid wise) of starting position
    result=abs(targetX+targetY)

    return (result,EXPECTED_RESULT)