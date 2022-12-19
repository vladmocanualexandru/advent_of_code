import sys, os, math, random, time

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(file):
    raw = getTuples_text(file, ' ')
    
    processed=raw

    return processed 

def getValue(op, memory):
    try:
        return int(op)
    except ValueError:
        return memory[op]

def runALULogic(instructions, input):
    memory = {"w":0,"x":0,"y":0,"z":0}

    inputPos = 0
    for instruction in instructions:
        command = instruction[0]

        if command == 'inp':
            memory[instruction[1]] = input[inputPos]
            # del input[0]
            inputPos+=1
        elif command == 'mul':
            memory[instruction[1]] *= getValue(instruction[2], memory)
        elif command == 'add':
            memory[instruction[1]] += getValue(instruction[2], memory)
        elif command == 'div':
            memory[instruction[1]] = math.floor(memory[instruction[1]] / getValue(instruction[2], memory))
        elif command == 'mod':
            memory[instruction[1]] %= getValue(instruction[2], memory)
        elif command == 'eql':
            memory[instruction[1]] = 1 if memory[instruction[1]] == getValue(instruction[2], memory) else 0
        else:
            log(red('Unknown command', command))

    return memory

PARAM_SETS = [
        [1,10,12],
        [1,12,7],
        [1,10,8],
        [1,12,8],
        [1,11,15],
        [26,-16,12],
        [1,10,8],
        [26,-11,13],
        [26,-13,3],
        [1,13,13],
        [26,-8,3],
        [26,-1,9],
        [26,-4,4],
        [26,-14,13]
    ]

def runALULogic2Module(input, params, z):
    pDiv = z % 26 + params[1]
    z = math.floor(z/params[0])

    if pDiv == input:
        return z
    else:
        return z*26 + input + params[2]

    # Phase 2
    # memory['x'] = 0 if memory['x'] == input else 1
    # memory['y'] = 25 * memory['x'] + 1
    # memory['z'] *= memory['y']
    # memory['y'] = (input + params[2]) * memory['x']
    # memory['z'] += memory['y']

    # Phase 1
    # memory['w'] = input
    # memory['x'] *= 0
    # memory['x'] += memory['z']
    # memory['x'] %= 26
    # memory['z'] = math.floor(memory['z']/params[0])
    # memory['x'] += params[1]
    # memory['x'] = 1 if memory['x'] == memory['w'] else 0
    # memory['x'] = 1 if memory['x'] == 0 else 0
    # memory['y'] *= 0
    # memory['y'] += 25
    # memory['y'] *= memory['x']
    # memory['y'] += 1
    # memory['z'] *= memory['y']
    # memory['y'] *= 0
    # memory['y'] += memory['w']
    # memory['y'] += params[2]
    # memory['y'] *= memory['x']
    # memory['z'] += memory['y']


def runALULogic2(modelNumber, paramSets):
    # Phase 3
    z = runALULogic2Module(modelNumber[0], paramSets[0], 0)
    for i in range(1,14):
        z=runALULogic2Module(modelNumber[i], paramSets[i], z)

    return z

def runALULogic3(modelNumber, paramSets):
    # Phase 4
    z5 = modelNumber[0] + paramSets[0][2]
    z5 = math.floor(z5/paramSets[1][0])*26+modelNumber[1] + paramSets[1][2]
    z5 = math.floor(z5/paramSets[2][0])*26+modelNumber[2] + paramSets[2][2]
    z5 = math.floor(z5/paramSets[3][0])*26+modelNumber[3] + paramSets[3][2]
    z5 = math.floor(z5/paramSets[4][0])*26+modelNumber[4] + paramSets[4][2]
    z5 = runALULogic2Module(modelNumber[5], paramSets[5], z5)
    z5 = math.floor(z5/paramSets[6][0])*26+modelNumber[6] + paramSets[6][2]
    z5 = runALULogic2Module(modelNumber[7], paramSets[7], z5)
    z5 = runALULogic2Module(modelNumber[8], paramSets[8], z5)
    z5 = math.floor(z5/paramSets[9][0])*26+modelNumber[9] + paramSets[9][2]
    z5 = runALULogic2Module(modelNumber[10], paramSets[10], z5)
    z5 = runALULogic2Module(modelNumber[11], paramSets[11], z5)
    z5 = runALULogic2Module(modelNumber[12], paramSets[12], z5)
    return runALULogic2Module(modelNumber[13], paramSets[13], z5)

def runALULogic2Module_lite(input, params, z):
    pDiv = z % 26 + params[1]
    z = math.floor(z/26)

    if pDiv == input:
        return z
    else:
        return z*26 + input + params[2]

def runALULogic3_lite(modelNumber, paramSets):
    # Phase 5
    z5 = modelNumber[0] + 12                                         # 0
    z5 = z5*26 + modelNumber[1] + 7                                  # U1
    z5 = z5*26 + modelNumber[2] + 8                                  # U2
    z5 = z5*26 + modelNumber[3] + 8                                  # U3
    z5 = z5*26 + modelNumber[4] + 15                                 # U4
    z5 = runALULogic2Module_lite(modelNumber[5], paramSets[5], z5)   # D4 -16
    z5 = z5*26 + modelNumber[6] + 8                                  # U5
    z5 = runALULogic2Module_lite(modelNumber[7], paramSets[7], z5)   # D5 -11
    z5 = runALULogic2Module_lite(modelNumber[8], paramSets[8], z5)   # D3 -13
    z5 = z5*26 + modelNumber[9] + 13                                 # U6
    z5 = runALULogic2Module_lite(modelNumber[10], paramSets[10], z5) # D6 -8
    z5 = runALULogic2Module_lite(modelNumber[11], paramSets[11], z5) # D2 -1
    z5 = runALULogic2Module_lite(modelNumber[12], paramSets[12], z5) # D1 -4
    z5 = runALULogic2Module_lite(modelNumber[13], paramSets[13], z5) # D0 -14

    return z5

def seedIsValid(seed):
    if seed[0]<3:
        return False
    if seed[1]>6:
        return False
    if seed[2]>2:
        return False
    if seed[3]<6:
        return False
    if seed[4]<2:
        return False
    if seed[5]<4:
        return False
    if seed[6]>4:
        return False
    
    return True

def nextSeed(seed):
    bypassLoop = True
    while bypassLoop or not seedIsValid(seed):
        bypassLoop = False
        seed[6]+=1
        for i in range(6, 0, -1):
            if seed[i]==10:
                seed[i]=1
                seed[i-1]+=1

        if seed[0]==10:
            return None
 
    return seed

def generateModelNumber(seed):
    modelNumber = [0 for i in range(14)]

    modelNumber[0]=seed[0]
    modelNumber[1]=seed[1]
    modelNumber[2]=seed[2]
    modelNumber[3]=seed[3]
    modelNumber[4]=seed[4]
    modelNumber[6]=seed[5]
    modelNumber[9]=seed[6]

    modelNumber[5]=modelNumber[4]-1
    modelNumber[7]=modelNumber[6]-3
    modelNumber[8]=modelNumber[3]-5
    modelNumber[10]=modelNumber[9]+5
    modelNumber[11]=modelNumber[2]+7
    modelNumber[12]=modelNumber[1]+3
    modelNumber[13]=modelNumber[0]-2

    return modelNumber

def solution(inputFile):
   
    instructions = getInputData(inputFile)

    seed = nextSeed([1 for i in range(7)])
    modelNumber = generateModelNumber(seed)

    runALULogic(instructions, modelNumber)
    runALULogic2(modelNumber, PARAM_SETS)
    runALULogic3(modelNumber, PARAM_SETS)
    runALULogic3_lite(modelNumber, PARAM_SETS)

    result = int(''.join([str(d) for d in modelNumber]))

    return (result, 31162141116841)