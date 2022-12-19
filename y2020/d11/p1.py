import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 2476

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')
    
    processed=raw

    return processed 

def solution(inputFile):
    seatsMat = getInputData(inputFile)

    # log('input sample (first 20)', seatsMat[:20])

    # matrixUtils.log(seatsMat, '', log)

    # rounds = 0
    seatChanged = True
    while seatChanged:
        seatChanged = False
        newSeatsMat = matrixUtils.generate(len(seatsMat), len(seatsMat[0]))
        for lineIndex in range(len(seatsMat)):
            for colIndex in range(len(seatsMat[lineIndex])):
                occupiedCount = sum(1 for s in matrixUtils.getNeighbors8(seatsMat, lineIndex,colIndex,False) if s == '#')

                if seatsMat[lineIndex][colIndex] == 'L' and occupiedCount == 0:
                    newSeatsMat[lineIndex][colIndex] = '#'
                    seatChanged = True
                elif seatsMat[lineIndex][colIndex] == '#' and occupiedCount>=4:
                    newSeatsMat[lineIndex][colIndex] = 'L'
                    seatChanged = True
                else:
                    newSeatsMat[lineIndex][colIndex] = seatsMat[lineIndex][colIndex]

        seatsMat = newSeatsMat

        # rounds +=1

    # matrixUtils.log(seatsMat, '', lambda e: log(green(e)))

    result=matrixUtils.addAll(seatsMat, lambda e: e=='#', lambda e: 1)

    return (result,EXPECTED_RESULT)