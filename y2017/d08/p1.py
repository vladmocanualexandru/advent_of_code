import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 6012

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' if ', ' ')
    
    processed=[ (r[0], r[1], int(r[2]), r[3], r[4], int(r[5])) for r in raw]

    return processed 

def validateCondition(register, parameters):
    regValue = register[parameters[0]]
    op = parameters[1]
    checkValue = parameters[2]

    if op == '!=':
        return regValue!=checkValue
    elif op == '==':
        return regValue==checkValue
    elif op == '<=':
        return regValue<=checkValue
    elif op == '>=':
        return regValue>=checkValue
    elif op == '<':
        return regValue<checkValue
    elif op == '>':
        return regValue>checkValue
    else:
        # log(red("Unknown operator", op))
        return None

def solution(inputFile):
    instructions = getInputData(inputFile)
    register = {}

    for instruction in instructions:
        if not instruction[0] in register:
            register[instruction[0]] = 0
        if not instruction[3] in register:
            register[instruction[3]] = 0

        if validateCondition(register, instruction[3:]):
            if instruction[1] == 'inc':
                register[instruction[0]] += instruction[2]
            elif instruction[1] == 'dec':
                 register[instruction[0]] -= instruction[2]
            # else:
            #     log(red("Unknown command", instruction[1]))

    # log(register)

    result=max([register[r] for r in register])
    return (result,EXPECTED_RESULT)

 

