import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 1501

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=[(entry[0], int(entry[1])) for entry in raw]

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    executedLines = []
    currentLine = 0

    acc = 0

    while currentLine>=0 and currentLine<len(inputData):
        if currentLine in executedLines:
            break

        executedLines.append(currentLine)

        command = inputData[currentLine]
        if command[0] == 'acc':
            acc+=command[1]
            currentLine+=1
        elif command[0] == 'jmp':
            currentLine+=command[1]
        else:
            currentLine+=1


    result=acc

    return (result, EXPECTED_RESULT)

 
