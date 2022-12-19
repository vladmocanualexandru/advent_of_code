import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 2257

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')
    
    processed=raw

    return processed

def findSeat(mat, y, x, deltaY, deltaX):
    y+=deltaY
    x+=deltaX
    while y>=0 and y<len(mat) and x>=0 and x<len(mat[0]):
        if mat[y][x]!='.':
            return mat[y][x]

        y+=deltaY
        x+=deltaX

    return '.'

def countOccupiedSeats(mat, y, x):

    count = 0

    count += 1 if findSeat(mat, y, x, -1, -1)=='#' else 0
    count += 1 if findSeat(mat, y, x, -1, 0)=='#' else 0
    count += 1 if findSeat(mat, y, x, -1, 1)=='#' else 0
    count += 1 if findSeat(mat, y, x, 0, -1)=='#' else 0
    count += 1 if findSeat(mat, y, x, 0, 1)=='#' else 0
    count += 1 if findSeat(mat, y, x, 1, -1)=='#' else 0
    count += 1 if findSeat(mat, y, x, 1, 0)=='#' else 0
    count += 1 if findSeat(mat, y, x, 1, 1)=='#' else 0

    return count

def solution(inputFile):
    seatsMat = getInputData(inputFile)

    # log('input sample (first 20)', seatsMat[:20])

    # matrixUtils.log(seatsMat, '', log)

    seatChanged = True
    while seatChanged:
        seatChanged = False
        newSeatsMat = matrixUtils.generate(len(seatsMat), len(seatsMat[0]))
        for lineIndex in range(len(seatsMat)):
            for colIndex in range(len(seatsMat[lineIndex])):
                occupiedCount = countOccupiedSeats(seatsMat, lineIndex, colIndex)

                if seatsMat[lineIndex][colIndex] == 'L' and occupiedCount == 0:
                    newSeatsMat[lineIndex][colIndex] = '#'
                    seatChanged = True
                elif seatsMat[lineIndex][colIndex] == '#' and occupiedCount>=5:
                    newSeatsMat[lineIndex][colIndex] = 'L'
                    seatChanged = True
                else:
                    newSeatsMat[lineIndex][colIndex] = seatsMat[lineIndex][colIndex]

        seatsMat = newSeatsMat

    # matrixUtils.log(seatsMat, '', lambda e: log(green(e)))

    result=matrixUtils.addAll(seatsMat, lambda e: e=='#', lambda e: 1)

    return (result,EXPECTED_RESULT)