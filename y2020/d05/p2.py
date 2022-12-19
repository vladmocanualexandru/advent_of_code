import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 629

def replaceLetters(text):
    return text.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=[replaceLetters(r) for r in raw]

    return processed 

def generateAllPossibleSeats():
    result = []
    for row in range(1,127):
        for seat in range(0,7):
            result.append(row*8+seat)

    return result

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[0])




    allPossibleSeats = generateAllPossibleSeats()
    for entry in inputData:
        id = int('0b'+entry[:7], 2) * 8 + int('0b'+entry[7:], 2)

        if id in allPossibleSeats: 
            allPossibleSeats.remove(id)

    result = []
    for i in range(1,len(allPossibleSeats)-1):
        if not allPossibleSeats[i-1]+1==allPossibleSeats[i] and not allPossibleSeats[i+1]-1==allPossibleSeats[i]:
            result.append(allPossibleSeats[i])
    
    return (result[0], EXPECTED_RESULT)

 
