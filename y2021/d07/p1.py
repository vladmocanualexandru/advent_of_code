import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,  ',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)

    result =  min([ sum(abs(c-position) for c in input) for position in range(min(input),max(input)+1) ])
    return (result,344605)