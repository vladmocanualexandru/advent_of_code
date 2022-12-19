# genius biscuit edition

import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

GEN_COUNT = 256

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,  ',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)

    counts = [0 for i in range(9)]

    for fish in input:
        counts[fish]+=1

    for gen in range(GEN_COUNT):
        fishParents = counts[0]

        for i in range(1,9):
            counts[i-1] = counts[i]

        counts[8] = fishParents
        counts[6] += fishParents

    result = sum(counts)

    return (result,1710166656900)