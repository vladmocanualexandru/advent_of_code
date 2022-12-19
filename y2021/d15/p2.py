import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 


def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, '')
  
    size = len(raw)

    newRaw = matrixUtils.generate(5*size, 5*size, 0)

    for y in range(size):
        for x in range(size):
            for k in range(5):
                for k2 in range(5):
                    newValue = (raw[y][x] + k+k2)
                    newValue += 1 if newValue>=10 else 0

                    newRaw[y+k*size][x+k2*size]=newValue%10


    return newRaw

    # return raw


def solution(inputFile):
    matrix = getInputData(inputFile)
    # matrixUtils.log(matrix, ' ', log, lambda e: ' ' if e == 0 else str(e))

    visited = matrixUtils.generate(len(matrix), len(matrix), 0)
    # matrixUtils.log(visited, ' ', log, lambda e: dark(e) if e == 0 else str(e))

    X = 100000
    distances = matrixUtils.generate(len(matrix), len(matrix), X)
    # matrixUtils.log(distances, ' ', log, lambda e: dark(e) if e == 1 else str(e))

    matrix = matrixUtils.wrap(matrix, 0)
    distances = matrixUtils.wrap(distances, 100000)
    visited = matrixUtils.wrap(visited, 1)

    distances[1][1] = 0

    nextPositions = {(1,1)}


    def getPosWithMinDistance():
        result = None
        minValue = X
        for pos in nextPositions:
            value = distances[pos[0]][pos[1]]
            if value<minValue:
                minValue = value
                result = pos

        return result


    while len(nextPositions)>0:

        (y,x) = getPosWithMinDistance()
        nextPositions.remove((y,x))

        currentDistance = distances[y][x]

        posN=(y-1, x)
        if visited[posN[0]][posN[1]]==0:
            distances[posN[0]][posN[1]]=min(currentDistance+matrix[posN[0]][posN[1]], distances[posN[0]][posN[1]])
            nextPositions.add(posN)

        posN=(y+1, x)
        if visited[posN[0]][posN[1]]==0:
            distances[posN[0]][posN[1]]=min(currentDistance+matrix[posN[0]][posN[1]], distances[posN[0]][posN[1]])
            nextPositions.add(posN)

        posN=(y, x-1)
        if visited[posN[0]][posN[1]]==0:
            distances[posN[0]][posN[1]]=min(currentDistance+matrix[posN[0]][posN[1]], distances[posN[0]][posN[1]])
            nextPositions.add(posN)

        posN=(y, x+1)
        if visited[posN[0]][posN[1]]==0:
            distances[posN[0]][posN[1]]=min(currentDistance+matrix[posN[0]][posN[1]], distances[posN[0]][posN[1]])
            nextPositions.add(posN)

        visited[y][x]=1
    
    result = distances[-2][-2]
    return (result,2842)
