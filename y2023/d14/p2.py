import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 105208
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    result = 0

    REPETITION FOUND
    
    map = getInputData(inputFile)

    iterations = 1000
    orientation = 0
    results = []

    for it in range(iterations):
        rockRolled = True
        while rockRolled:
            rockRolled = False

            for lineIndex in range(1,len(map),1):
                for colIndex in range(len(map[0])):
                    if map[lineIndex][colIndex] == 'O' and map[lineIndex-1][colIndex] == '.':
                        map[lineIndex-1][colIndex] = 'O'
                        map[lineIndex][colIndex] = '.'
                        rockRolled = True

        result = 0
        for lineIndex in range(len(map)):
            for colIndex in range(len(map[0])):
                if map[lineIndex][colIndex] == 'O':
                    result += len(map) - lineIndex

        resultTuple = (result, orientation)
        if resultTuple in results:
            log(green("BINGO! iteration=", it,  resultTuple))

        results.append(resultTuple)

        map = matrixUtils.rotate(map, 1)
        orientation = (orientation+1)%4

    # logMatrix(map)

    # log(red())
    return (result, EXPECTED_RESULT)