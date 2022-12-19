import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def calculateFuel(crabPosition, destination):
    distance = abs(crabPosition-destination)
    return distance*(distance+1)/2

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,  ',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)
    # input = [16,1,2,0,4,2,7,1,2,14]
    
    result = int(min([ sum(calculateFuel(c, position) for c in input) for position in range(min(input), max(input)+1)]))

    return (result, 93699985)