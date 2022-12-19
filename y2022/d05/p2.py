import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = "QNDWLMGNS"

def getInputData(inputFile):
    raw = getRawLines(inputFile)

    initialConfig = []
    commands = []

    saveInCommands = False
    for line in raw:
        if line.strip() == '':
            saveInCommands = True
            continue

        if not saveInCommands:
            initialConfig.append(line)
        else:
            s = pd.Series(line.split(' ')).iloc[[1,3,5]]
            commands.append((int(s.iloc[0]),int(s.iloc[1])-1,int(s.iloc[2])-1))

    initialConfig=matrixUtils.flipHorizontal(matrixUtils.flipMainDiagonal(initialConfig))
    
    stacks = []
    for line in initialConfig:
        if line[0].isnumeric():
            stacks.append(''.join(line).strip()[1:])

    processed = (stacks,commands)
    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    stacks = inputData[0]
    commands = inputData[1]

    for command in commands:
        payload = stacks[command[1]][0-command[0]:]

        # log(payload)
        stacks[command[1]] = stacks[command[1]][:0-command[0]]
        stacks[command[2]] += payload

    # log(stacks)

    result=''.join([s[-1] for s in stacks])

    return (result,EXPECTED_RESULT)