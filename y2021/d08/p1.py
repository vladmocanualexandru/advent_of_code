import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' | ')
    
    processed=[i[1].split(' ') for i in raw]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)

    result = 0

    acceptedLengths = [2,4,3,7]
    for digitQuad in input:
        result += sum(1 for digit in digitQuad if len(digit) in acceptedLengths)

    return (result,375)