import math
from utils.terminalUtils import *
from utils.solutionRoot import *
 
# OP CODES
# CBADE
# xxx01 - addition - op1, op2, destination - 3 parameters
# xxx02 - multiplication - op1, op2, destination - 3 parameters
# xxx03 - input - destination - 1 parameter
# xxx04 - output - source - 1 parameter
# xxx05 - jump if true - 2 parameters
# xxx06 - jump if false - 2 parameters
# xxx07 - less than - 3 parameters - if first is less than second, stores 1 in position, otherwise stores 0
# xxx08 - equals - 3 parameters - if first is equal to the second, stores 1 in position, otherwise stores 0
# xxx09 - set relative base - 1 parameter - the value to be added to the relative base
# xxx99 - halt - 0 parameters
#
# DE - instruction code
# A,B,C - mode for 1st, 2nd, 3rd parameter -> 0=position mode, 1=immediate mode, 2=relative mode (position mode + relative base)

OP_CODE_PARAMS = [-1,4,4,2,2,3,3,4,4,2]

def getValue(mem, op, type):
    instructions = mem["instructions"]

    result = None
    if type == '0':
        if op<len(instructions):
            result = instructions[op]
        else:
            if not op in mem["extraMemory"]:
                mem["extraMemory"][op] = 0
            result = mem["extraMemory"][op]
    elif type == '1':
        result = op
    elif type == '2':
        op += mem["relativeBase"]
        if op<len(instructions):
            result = instructions[op]
        else:
            if not op in mem["extraMemory"]:
                mem["extraMemory"][op] = 0
            result = mem["extraMemory"][op]
    else:
        log(red("Unknown op type", type))
    
    return result

def getValues(mem, op1, op2, paramTypes):
    val1 = getValue(mem, op1, paramTypes[0])
    val2 = getValue(mem, op2, paramTypes[1])

    return (val1, val2)

def write(mem, pos, type, value):
    if type == '2':
        pos += mem["relativeBase"]

    if pos<len(mem['instructions']):
        mem["instructions"][pos] = value
    else:
        mem["extraMemory"][pos] = value

def initializeMemory(instructions, input=[]):
    return {
        "currentPos" : 0,
        "instructions" : instructions,
        "relativeBase" : 0,
        "input" : input,
        "extraMemory" : {}
    }

# logLevel 0 = silent
# logLevel 1 = input/output logs
# logLevel 2 = op logs
def run(mem, logLevel=1):
    
    currentPos = mem["currentPos"]
    instructions = mem["instructions"]

    outputs = []

    while currentPos<len(instructions) and instructions[currentPos] != 99:
        opcode = instructions[currentPos]%100
        paramTypes = ('%03d' % math.floor(instructions[currentPos]/100))[::-1]

        jumpSteps = OP_CODE_PARAMS[opcode]

        ops = getValues(mem, instructions[currentPos+1], instructions[currentPos+2], paramTypes)

        if logLevel>=2:
            log(dark(instructions[currentPos], opcode, ops, '(%s)' % paramTypes))

        if opcode == 1: # addition
            write(mem, instructions[currentPos+3], paramTypes[2], ops[0]+ops[1])
        elif opcode == 2: # multiplication
            write(mem, instructions[currentPos+3], paramTypes[2], ops[0]*ops[1])
        elif opcode == 3: # input
            if len(mem['input']) == 0:
                if logLevel>=1:
                    log(blue('WAITING FOR INPUT'))
                return ('WAIT', outputs)
            else:
                if logLevel>=1:
                    log(blue('INPUT %d' % mem["input"][0]))

                write(mem, instructions[currentPos+1], paramTypes[0], mem["input"][0])

                del mem["input"][0]
        elif opcode == 4: # output
            if logLevel>=1:
                log(green('OUTPUT %d' % ops[0]))

            outputs.append(ops[0])
        elif opcode == 5: # jump if diff from 0
            if ops[0]!=0:
                mem["currentPos"] = currentPos = ops[1]
                jumpSteps=0
        elif opcode == 6: # jump if eq to 0
            if ops[0]==0:
                mem["currentPos"] = currentPos = ops[1]
                jumpSteps=0
        elif opcode == 7: # write 1, if a less than b, else 0 
            write(mem, instructions[currentPos+3], paramTypes[2], 1 if ops[0]<ops[1] else 0)

        elif opcode == 8: # write 1, if a eq to b, else 0
            write(mem, instructions[currentPos+3], paramTypes[2], 1 if ops[0]==ops[1] else 0)

        elif opcode == 9: # adjust relative base
            mem["relativeBase"] += ops[0]
        else:
            log(red('Unknown op code', opcode))
            return ('FAIL', outputs)

        mem["currentPos"] = currentPos = currentPos + jumpSteps

    return ('OK', outputs)