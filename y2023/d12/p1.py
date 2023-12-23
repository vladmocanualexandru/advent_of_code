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

EXPECTED_RESULT = 7260
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')
    
    processed=[(entry[0], [int(e) for e in entry[1].split(',')]) for entry in raw]

    return processed 

def checkSprings(springs, meta):
    counts = [len(e) for e in springs.split('.') if e != '']
    return counts == meta

def buildSprings(springs, index, meta):
    count = 0
    if index < len(springs):
        if springs[index] == '?':
            count+=buildSprings("%s#%s"%(springs[:index],springs[index+1:]), index+1, meta)
            count+=buildSprings("%s.%s"%(springs[:index],springs[index+1:]), index+1, meta)

            return count
        else:
            return buildSprings(springs, index+1, meta)
    else:
        return 1 if checkSprings(springs, meta) else 0

def solution(inputFile):
    result = 0
    
    for (springs, meta) in getInputData(inputFile):
        # log(green(springs, meta))

        result+=buildSprings(springs,0,meta)
        

    # log(red())
    return (result, EXPECTED_RESULT)