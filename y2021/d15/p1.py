import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 


def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, '')
    raw = matrixUtils.wrap(raw, 0)
    return raw

def solution(inputFile):
    matrix = getInputData(inputFile)
    # matrixUtils.log(matrix, ' ', log)

    distances = matrixUtils.generate(len(matrix),len(matrix),'-')
    # distances[1][1]=0

    neighborQueue=[(1,1)]

    while len(neighborQueue)>0:
        (x,y) = neighborQueue.pop(0)

        if matrix[y][x] == 0 or distances[y][x]!='-':
            continue

        neighborValues = [e for e in [distances[y-1][x],distances[y+1][x],distances[y][x-1],distances[y][x+1]] if e != '-']
        distance = matrix[y][x]

        if len(neighborValues)>0:
            distance += min(neighborValues)

        if y==x==1:
            distances[y][x] = 0
        else:
            distances[y][x] = distance


        neighborQueue.append((y,x+1))
        neighborQueue.append((y+1,x))

    # matrixUtils.log(distances, ' ', log, (lambda e: ' -' if e =='-' else ('{:02d}'.format(int(e)))))

    result = distances[len(matrix)-2][len(matrix)-2]

    return (result,435)