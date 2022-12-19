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
 
EXPECTED_RESULT = 4350000000957
GENERATIONS = 100000
PREFIX='.....'

def getInputData(inputFile):
    raw = getStrings(inputFile)

    rulesDict = {}
    for rule in [entry.split(" => ") for entry in raw[2:]]:
        rulesDict[rule[0]] = rule[1]
    
    return (raw[0][15:], rulesDict) 

def solution(inputFile):
    (pots, rules) = getInputData(inputFile)

    pots = PREFIX+pots+"......"

    diffHistory = [-1 for i in range(3)]

    # log('Searching for generation growth stabilization...')
    
    growthValue = None
    oldResult = -1
    newResult = -1
    genCount = 0
    while growthValue is None:
        newPots = "...."

        for potIndex in range(2,len(pots)-2):
            config = pots[potIndex-2:potIndex+3]

            if config in rules:
                newPots+=rules[config]
            else:
                newPots+='.'

        pots = newPots+"...."

        genCount+=1

        if (genCount)%100 == 0:
            newResult = 0

            for potIndex in range(len(pots)):
                if pots[potIndex] == '#':
                    newResult+=potIndex-genCount*2-len(PREFIX)

            diffHistory.pop(0)
            diffHistory.append(newResult-oldResult)
            oldResult = newResult

            for i in range(1,len(diffHistory)):
                if diffHistory[i-1]!=diffHistory[i]:
                    break
            else:
                growthValue = diffHistory[-1]

            # log(diffHistory)

    # log('Generation growth stabilized %d @gen #%d' % (growthValue, genCount))

    result = int((5*pow(10,10)-genCount)/100*growthValue+newResult)

    return (result,EXPECTED_RESULT)