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

    STEPS = 50
    WRAP_SIZE = 60

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

        return matrixUtils.wrap(matrixUtils.trim(newMatrix), newMatrix[1][-2])


    for i in range(STEPS):
        # log(i)
        matrix = getNewMatrix(matrix)

    result = matrixUtils.addAll(matrix, lambda e : e == '#', lambda e : 1)

    # just for fun! Making nice vizualizations! :D
    weightMatrix = matrixUtils.generate(len(matrix), len(matrix), 0)

    for y in range(len(matrix)):
        for x in range(len(matrix)):
            weightMatrix[y][x] = sum([1 for n in matrixUtils.getNeighbors8(matrix, y, x, True) if n == '#'])

            

    # matrixUtils.log(weightMatrix, '' , log, lambda e: blue(C_BLOCK) if e == 0 else ( light(C_BLOCK) if e >6 else ( green(C_BLOCK) if e >3 else yellow(C_BLOCK))))

    return (result,15714)

 
