import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ',', '=')
    return raw

def foldX(matrix, x):
    for line in range(len(matrix)):
        for col in range(x+1, len(matrix[-1])):
            matrix[line][x - (col-x)] |= matrix[line][col]

        for col in range(x, len(matrix[-1])):
            matrix[line].pop()


    return

def foldY(matrix, y):
    for line in range(y+1,len(matrix)):
        for col in range(len(matrix[-1])):
            matrix[y - (line-y)][col]|= matrix[line][col]

    for line in range(y, len(matrix)):
        matrix.pop()


    return


logMap = [C_DOT_TRANSPARENT, C_DOT_FULL, green(C_VERT_LINE),red(C_HORIZ_LINE)]

def solution(inputFile):
    inputData = getInputData(inputFile)

    dots = []
    folds = []

    maxX = maxY = 0
    for entry in inputData:
        if not 'fold' in entry[0]:
            dots.append((int(entry[0]),int(entry[1])))

            maxX = max(maxX, dots[-1][0])
            maxY = max(maxY, dots[-1][1])
        else:
            folds.append((entry[0], int(entry[1])))

    matrix = matrixUtils.generate(maxY+1,maxX+1, 0)

    for dot in dots:
        matrix[dot[1]][dot[0]] = 1

    # matrixUtils.log(matrix, '', log)

    for fold in folds:
        # log(fold)
        

        if fold[0] == 'fold along x':
            matrixUtils.setAreaToValue(matrix, 0, fold[1], len(matrix), fold[1]+1, 2)
            # matrixUtils.log(matrix,'',log,lambda e:logMap[e])

            # input('Fold?')

            foldX(matrix, int(fold[1]))
        else:
            matrixUtils.setAreaToValue(matrix, fold[1], 0, fold[1]+1, len(matrix[0]), 3)
            # matrixUtils.log(matrix,'',log,lambda e:logMap[e])
            # input('Fold?')

            foldY(matrix, int(fold[1]))

        # matrixUtils.log(matrix,'',log,lambda e:logMap[e])
        # input('Next?')

        break

    return (matrixUtils.addAll(matrix),638)