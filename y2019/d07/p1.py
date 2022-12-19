import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))
sys.path.append(os.path.abspath(os.path.join('..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

import y2019.int_code_computer as int_code_computer
 
EXPECTED_RESULT = 255590

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    return processed 

def computeSequence(program, sequence):
    # log(purple("Sequence %s" % str(sequence)))
    ampInput = 0
    for ampCount in range(5):
        # log("Amp ", ampCount)

        mem = int_code_computer.initializeMemory([]+program,[sequence[ampCount], ampInput])
        ampInput = int_code_computer.run(mem, 0)[1][0]

    # log(purple("Signal value %d" % ampInput))
    return ampInput

def distinctDigits(sequence):
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            if sequence[i] == sequence[j]:
                return False

    return True

def nextSequence(sequence):
    if sequence == None:
        return None

    newSequence = []+sequence

    while True:
        newSequence[4] += 1

        if newSequence[4] == 5:
            newSequence[4] = 0
            newSequence[3] += 1
        
        if newSequence[3] == 5:
            newSequence[3] = 0
            newSequence[2] += 1

        if newSequence[2] == 5:
            newSequence[2] = 0
            newSequence[1] += 1

        if newSequence[1] == 5:
            newSequence[1] = 0
            newSequence[0] += 1
        
        if newSequence[0] == 5:
            return None

        if distinctDigits(newSequence):
            break

    return newSequence

def solution(inputFile):
    program = getInputData(inputFile)

    sequence = [0,1,2,3,4]

    result = -1
    while sequence != None:
        result=max(result, computeSequence(program, sequence))
        sequence = nextSequence(sequence)

    return (result,EXPECTED_RESULT)

 
