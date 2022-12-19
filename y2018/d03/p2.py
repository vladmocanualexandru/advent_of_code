import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 412 

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

def drawClaim(claim, matrix, marker, claimOverlap):
    for lineI in range(claim[1], claim[1]+claim[3]):
        for colI in range(claim[0], claim[0]+claim[2]):
            if matrix[lineI][colI] == '.':
                matrix[lineI][colI] = marker
            else:
                claimOverlap[marker] = 1
                claimOverlap[matrix[lineI][colI]] = 1

def solution(inputFile):
    inputData = getInputData(inputFile)

    claims = inputData[0]
    # log('sample', claims[:10])
    
    width = inputData[1]
    height = inputData[2]

    matrix = matrixUtils.generate(height, width, '.')

    claimOverlap = [0 for i in range(len(claims))]

    for marker in range(len(claims)):
        drawClaim(claims[marker], matrix, marker, claimOverlap)

    result = matrixUtils.find([claimOverlap], lambda e: e, lambda e: e==0)

    # log(blue("Result indicates position - id is position+1"))

    return (result[0][1]+1,EXPECTED_RESULT)

 
