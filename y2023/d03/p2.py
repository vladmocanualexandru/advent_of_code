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

EXPECTED_RESULT = 82824352
 
def getInputData(inputFile):

    raw = getTuples_text(inputFile, '')

    processed=matrixUtils.wrap(raw, '.')

    return processed 

def containsSymbol(arr):
    for elem in arr:
        if elem == '*':
            return True
    return False

def solution(inputFile):
    mat = getInputData(inputFile)

    # build numbers -> cog coords dictionary
    numbers = []
    lines = len(mat)
    cols = len(mat[0])
    number = 0
    cogs = []
    for lineIndex in range(1,lines-1, 1):
        for colIndex in range(1,cols-1, 1):
            cell = mat[lineIndex][colIndex]
            if cell.isdigit():
                number*=10
                number+=int(cell)

                cogs += [entry[1] for entry in matrixUtils.getNeighbors8(mat, lineIndex, colIndex, False, 1, True) if entry[0]=='*' and not entry[1] in cogs]
            else:
                if number!=0:
                    if len(cogs)>0:
                        numbers.append((number, cogs))
                    
                    number = 0
                    cogs = []

    # build cogid (y*1000+x) -> number dictionary
    cogs = {}
    for number in numbers:
        for cog in number[1]:
            cogId = cog[0]*1000+cog[1]
            if not cogId in cogs:
                cogs[cogId] = []
            cogs[cogId].append(number[0])
    
    # consider just cogs connected to 2 numbers, sum the multiplied numbers
    result = sum([cogs[cogid][0]*cogs[cogid][1] for cogid in cogs if len(cogs[cogid])==2 ])

    return (result, EXPECTED_RESULT)