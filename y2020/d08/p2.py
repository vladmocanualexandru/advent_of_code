import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 509

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=[(entry[0], int(entry[1])) for entry in raw]

    return processed 

def testCode(inputData):
    executedLines = []
    currentLine = 0

    acc = 0

    while currentLine>=0 and currentLine<len(inputData):
        if currentLine in executedLines:
            return None

        executedLines.append(currentLine)

        command = inputData[currentLine]
        if command[0] == 'acc':
            acc+=command[1]
            currentLine+=1
        elif command[0] == 'jmp':
            currentLine+=command[1]
        else:
            currentLine+=1

    return acc

def adjustCode(inputData, commandIndex):
    while not inputData[commandIndex][0] in ['nop', 'jmp'] and commandIndex<len(inputData):
        commandIndex+=1

    switchCommand(inputData, commandIndex)

    return commandIndex+1

def switchCommand(inputData, commandIndex):
    inputData[commandIndex] = ({'nop':'jmp', 'jmp':'nop'}[inputData[commandIndex][0]], inputData[commandIndex][1])


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result = None
    commandIndex = adjustCode(inputData, 0)

    while commandIndex<len(inputData) and result is None:
        result=testCode(inputData)

        if result is None:
            switchCommand(inputData, commandIndex-1)

            commandIndex = adjustCode(inputData, commandIndex)

    return (result, EXPECTED_RESULT)

 
