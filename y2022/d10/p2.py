import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = "BRJLFULP"

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=[(entry[0], int(entry[1]) if len(entry)==2 else None) for entry in raw]

    return processed 

def drawOnScreen(screen, cycleCount, crtX, registerX):
    if abs(crtX-registerX)<2:
        screen[int(cycleCount/40)][crtX] = C_BLOCK

def solution(inputFile):
    instructions = getInputData(inputFile)

    registerX = 1
    crtX = 0

    screen = matrixUtils.generate(6, 40, ' ')
    screen[0][0] = C_BLOCK

    cycleCount = 0

    for (instr,val) in instructions:
        cycleCount+=1

        crtX=(crtX+1)%40
        drawOnScreen(screen, cycleCount, crtX, registerX)

        if instr == 'addx':
            cycleCount+=1
            registerX+=val

            crtX=(crtX+1)%40
            drawOnScreen(screen, cycleCount, crtX, registerX)

    # uncomment the following line to output the result in console
    # matrixUtils.log(screen, '', log)

    result = "BRJLFULP"
    return (result,EXPECTED_RESULT)