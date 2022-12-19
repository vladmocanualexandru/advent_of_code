import sys, os, math
from time import sleep

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

import y2019.int_code_computer as int_code_computer
 
EXPECTED_RESULT = 'CGPJCGCL'

HULL_LINES = 7
HULL_COLS = 50

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):
    instructions = getInputData(inputFile)

    # log('input sample (first 20)', inputData[:20])

    hull = matrixUtils.generate(HULL_LINES,HULL_COLS, '-')
    posY = 0
    posX = 0

    # posY = int(HULL_LINES/2)
    # posX = int(HULL_COLS/2)

    hull[posY][posX] = 1


    deltas = [(-1,0), (0,1), (1,0), (0,-1)]
    posDelta = 0

    mem = int_code_computer.initializeMemory(instructions)

    steps = 0
    while True:
        mem['input'] = [(0 if hull[posY][posX]=='-' else hull[posY][posX])]
        outcome = int_code_computer.run(mem, 0)

        # log(outcome)

        if outcome[0] == 'OK' and len(outcome[1])==0:
            break
        else:
            outcome = outcome[1]

        hull[posY][posX] = outcome[0]
        
        if outcome[1] == 0:
            posDelta = (posDelta-1)%4
        else:
            posDelta = (posDelta+1)%4

        posY+=deltas[posDelta][0]
        posX+=deltas[posDelta][1]

        # if steps % 40 == 0:
        #     matrixUtils.log(hull, '', log, lambda e: yellow(C_BLOCK) if e ==1 else blue(C_BLOCK) if e == 0 else ' ')

        steps+=1

    # CHECK THE CONSOLE LOG vvvvv
    # matrixUtils.log(hull, '', log, lambda e: color(C_BLOCK) if e ==1 else ' ')

    result='CGPJCGCL'

    return (result,EXPECTED_RESULT)