import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=[r for r in raw]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)

    aim = 0
    distance = 0
    depth = 0

    for index in range(len(input)):
        command = input[index][0]
        value = int(input[index][1])

        if command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
        else:
            distance += value
            depth += aim*value

    # log("aim: ", aim)
    # log("distance: ", distance)
    # log("depth: ", depth)

    result = distance*depth
    return (result, 2044620088)