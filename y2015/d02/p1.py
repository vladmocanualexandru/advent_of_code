import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1586300

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'x')
    
    processed=raw

    return processed 

def calculateArea(numberTuple):
    area = numberTuple[0]*numberTuple[1]
    minArea = area
    totalArea = 2*area

    area = numberTuple[1]*numberTuple[2]
    if area<minArea:
        minArea = area
    totalArea+=2*area

    area = numberTuple[0]*numberTuple[2]
    if area<minArea:
        minArea = area
    totalArea+=2*area

    totalArea+=minArea

    return totalArea


def solution(inputFile):

    inputData = getInputData(inputFile)

    result = 0

    for tuple in inputData:
        result += calculateArea(tuple)

    return (result, EXPECTED_RESULT)

 