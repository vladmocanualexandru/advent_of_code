import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')

    matrix = []

    for i in range(2, len(raw)):
        matrix.append(raw[i])

    return (raw[0], matrix)


def solution(inputFile):

    STEPS = 2
    WRAP_SIZE = 10

    inputData = getInputData(inputFile)

    algo = inputData[0]

    matrix = matrixUtils.wrap(inputData[1], '.', WRAP_SIZE)

    def getAlgoChar(chars):
        result = int(''.join([(lambda c: '1' if c =='#' else '0')(c) for c in chars]),2)
        return algo[result] 


    def getNewMatrix(matrix):
        newMatrix = matrixUtils.generate(len(matrix),len(matrix),'.')

        for y in range(0, len(matrix)):
            for x in range(0, len(matrix)):
                newMatrix[y][x] = getAlgoChar(matrixUtils.getNeighbors8(matrix, y, x, True))

        return newMatrix






    # matrixUtils.log(matrix, '' , log, lambda e: C_DOT_FULL if e =='#' else ' ')

    for i in range(STEPS):
        matrix = getNewMatrix(matrix)
        # log('NewMatrix:')
        # matrixUtils.log(matrix, '' , log, lambda e: C_DOT_FULL if e =='#' else ' ')

    result = 0

    # log('NewMatrix:')
    # matrixUtils.log(matrix, '' , log, lambda e: C_DOT_FULL if e =='#' else ' ')
    
    for line in matrix[1:-1]:
        result += sum([1 for c in line[1:-1] if c == '#'])

    return (result,5249)