import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

WRAP_MATERIAL = ' '

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'')
    
    processed=raw

    return processed 

def solution(inputFile):

    matrix = matrixUtils.wrap(getInputData(inputFile), WRAP_MATERIAL)

    # matrixUtils.log(matrix, ' ', log, lambda e : light(e) if e == 0 else dark(e))

    neighborCoordDeltas = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1),(1,-1), (1,0), (1,1)]

    result = 1
    resultFound = False
    while not resultFound:
        flashCoords = matrixUtils.find(matrix, (lambda e : (e+1)%10 if e!=WRAP_MATERIAL else WRAP_MATERIAL), lambda e: e==0)

        # matrixUtils.log(matrix, ' ', log, (lambda e : yellow(e) if e == 0 else (light(e) if e  == 9 else dark(e))))

        fCoordIndex = 0
        while fCoordIndex<len(flashCoords):
            fCoord = flashCoords[fCoordIndex]
            for nCoordDelta in  neighborCoordDeltas:
                nCoord = (fCoord[0]+nCoordDelta[0],fCoord[1]+nCoordDelta[1])

                if matrix[nCoord[0]][nCoord[1]] != WRAP_MATERIAL and matrix[nCoord[0]][nCoord[1]]!=0:
                    matrix[nCoord[0]][nCoord[1]]=(matrix[nCoord[0]][nCoord[1]]+1)%10

                    if matrix[nCoord[0]][nCoord[1]]==0:
                        flashCoords.append(nCoord)

            fCoordIndex+=1

        # matrixUtils.log(matrix, ' ', log, (lambda e : yellow(e) if e == 0 else (light(e) if e  == 9 else dark(e))))

        if matrixUtils.addAll(matrix, lambda e : e!=WRAP_MATERIAL)==0:
            resultFound = True
        else:
            result+=1

    return (result,216)