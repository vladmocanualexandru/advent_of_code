import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 118223 

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,' @ ', ': ', ',', 'x', '#')

    width = minX = raw[0][2]
    height = minY = raw[0][3]

    for entry in raw:
        minX = min(minX, entry[2])
        width = max(width, entry[2]+entry[4])
        minY = min(minY, entry[3])
        height = max(height, entry[3]+entry[5])

    processed = [(a[2]-minX, a[3]-minY, a[4], a[5]) for a in raw]

    width-=minX
    height-=minY

    return (processed, width, height) 

def drawClaim(claim, matrix, marker):
    for lineI in range(claim[1], claim[1]+claim[3]):
        for colI in range(claim[0], claim[0]+claim[2]):
            if matrix[lineI][colI] == '.':
                matrix[lineI][colI] = marker
            else:
                matrix[lineI][colI] = 'X'

def solution(inputFile):
    inputData = getInputData(inputFile)

    claims = inputData[0]
    # log('sample', claims[:10])
    
    width = inputData[1]
    height = inputData[2]

    matrix = matrixUtils.generate(height, width, '.')

    marker = 0
    for claim in claims:
        drawClaim(claim, matrix, marker)

        marker = (marker+1)%6

    # matrixUtils.log(matrixUtils.trim(matrix, 100), '', log, lambda e: ' ' if e == '.' else (light(C_BLOCK) if e == 'X' else formatOutput(availableColorCodes[e+1], C_BLOCK)))

    # result = matrixUtils.addAll(matrixUtils.trim(matrix, 200), lambda e: e=='X', lambda e: 1)
    result = matrixUtils.addAll(matrix, lambda e: e=='X', lambda e: 1)

    return (result,EXPECTED_RESULT)

 
