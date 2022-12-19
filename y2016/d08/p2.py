import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 'CFLELOYFCS'

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=raw

    return processed 

matrix = [[' ' for j in range(50)] for i in range(6)]

def printMatrix():
    for line in matrix:
        log(''.join(line))

def rect(dimensions):
    for i in range(dimensions[1]):
        for j in range(dimensions[0]):
            matrix[i][j]='█'

def rotateRow(lineNumber, offset):
    for counter in range(offset):
        lastValue = matrix[lineNumber][-1]

        for j in range(len(matrix[lineNumber])-1, 0, -1):
            matrix[lineNumber][j]=matrix[lineNumber][j-1]

        matrix[lineNumber][0] = lastValue

def rotateColumn(colNumber, offset):
    for counter in range(offset):
        lastValue = matrix[-1][colNumber]

        for j in range(len(matrix)-1, 0, -1):
            matrix[j][colNumber]=matrix[j-1][colNumber]

        matrix[0][colNumber] = lastValue

def solution(inputFile):
    commands = getInputData(inputFile)

    for command in commands:
        if command[0]=='rect':
            rect([int(coord) for coord in command[1].split('x')])
        elif command[1]=='row':
            rotateRow(int(command[2].split('=')[1]), int(command[4]))
        else:
            rotateColumn(int(command[2].split('=')[1]), int(command[4]))

    # printMatrix()

    # uncomment above command for result
    return ("CFLELOYFCS",EXPECTED_RESULT)


 