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
 
EXPECTED_RESULT = 12980

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=[(entry[0], int(entry[1]) if len(entry)==2 else None) for entry in raw]

    return processed 

def solution(inputFile):
    instructions = getInputData(inputFile)

    registerX = 1

    cycleCount = 0
    result=0

    for (instr,val) in instructions:
        # log(dark(instr, val))

        cycleCount+=1
        if cycleCount==20 or (cycleCount-20)%40 == 0:
            # log(green(cycleCount, registerX, cycleCount*registerX))
            result+=cycleCount*registerX

        if instr == 'addx':
            cycleCount+=1
            if cycleCount==20 or (cycleCount-20)%40 == 0:
                # log(green(cycleCount, registerX, cycleCount*registerX))
                result+=cycleCount*registerX

            registerX+=val

    return (result,EXPECTED_RESULT)