import sys, os, math, time
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 102943

CONSECUTIVE_REPETITIONS_GOAL = 5
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    result = 0

    # After x iterations a sequence of y iterations is repeated; 
    # Solution: find x and y; result: iteration #( (1000000000 - x) % y )
    
    map = getInputData(inputFile)

    iterations = int(math.pow(10,9))
    # iterations = 3
    results = []

    log("Searching for repetitions...")
    consecutiveRepetitions = 0
    repetitionIndex = -1
    repetitionLength = -1

    for it in range(iterations):
        for orientation in range(4):
            rockRolled = True
            while rockRolled:
                rockRolled = False

                for lineIndex in range(1,len(map),1):
                    for colIndex in range(len(map[0])):
                        if map[lineIndex][colIndex] == 'O' and map[lineIndex-1][colIndex] == '.':
                            map[lineIndex-1][colIndex] = 'O'
                            map[lineIndex][colIndex] = '.'
                            rockRolled = True

            map = matrixUtils.rotate(map, 1)

        result = 0
        for lineIndex in range(len(map)):
            for colIndex in range(len(map[0])):
                if map[lineIndex][colIndex] == 'O':
                    result += len(map) - lineIndex

        resultTuple = (result, orientation)
        
        if resultTuple in results:
            consecutiveRepetitions+=1
        else:
            consecutiveRepetitions = 0

        results.append(resultTuple)

        if consecutiveRepetitions==CONSECUTIVE_REPETITIONS_GOAL:
            repetitionIndex = it + 1 - CONSECUTIVE_REPETITIONS_GOAL
            log(CONSECUTIVE_REPETITIONS_GOAL, " repetitions found @ iteration ", repetitionIndex)
            break

        # log(resultTuple)

    # logMatrix(map)
    # exit()

    log("Searching first appearance of repetition sequence...")

    fSeqFound = False
    startIt = 0
    while not fSeqFound:
        # log(startIt)
        for it2 in range(CONSECUTIVE_REPETITIONS_GOAL):
            # log(startIt+it2,repetitionIndex+it2)
            if results[startIt+it2] != results[repetitionIndex+it2]:
                break
        else:
            log("First sequence found!")
            repetitionLength = repetitionIndex-startIt
            repetitionIndex = startIt
            fSeqFound = True
        
        startIt+=1

    log("Repeating sequence found, length ", repetitionLength, " starting with iteration ",repetitionIndex)

    result = results[repetitionIndex + (iterations-repetitionIndex)%repetitionLength-1][0]
    # logMatrix(map)

    # log(red())
    return (result, EXPECTED_RESULT)