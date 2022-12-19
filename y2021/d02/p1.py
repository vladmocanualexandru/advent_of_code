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

    distance = 0
    depth = 0

    for tuple in input:
        command = tuple[0]
        value = int(tuple[1])

        if command == 'up':
            depth-=value
        elif command == 'down':
            depth+=value
        else:
            distance += value

    # log("distance:", distance)
    # log("depth:", depth)

    return (distance*depth,2147104)