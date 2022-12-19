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
 
EXPECTED_RESULT = 2952
GENERATIONS = 20
PREFIX='.....'

def getInputData(inputFile):
    raw = getStrings(inputFile)

    rulesDict = {}
    for rule in [entry.split(" => ") for entry in raw[2:]]:
        rulesDict[rule[0]] = rule[1]
    
    processed=[entry.replace("#", "1").replace(".", "0").split(" => ") for entry in raw[2:]]

    return (raw[0][15:], rulesDict) 

def solution(inputFile):
    (pots, rules) = getInputData(inputFile)

    pots = PREFIX+pots+"......"

    # log(pots)
    # log(rules)

    for genCount in range(GENERATIONS):
        newPots = "...."

        for potIndex in range(2,len(pots)-2):
            config = pots[potIndex-2:potIndex+3]
            # log(config)

            if config in rules:
                newPots+=rules[config]
            else:
                newPots+='.'

        pots = newPots+"...."
        # log(pots)

    result = 0
    for potIndex in range(len(pots)):
        if pots[potIndex] == '#':
            result+=potIndex-GENERATIONS*2-len(PREFIX)

    return (result,EXPECTED_RESULT)