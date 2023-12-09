import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 15299095336639
 
def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[entry for entry in raw[2:]]
    nodes = {}
    startingNodes = []

    for line in processed:
        [node, links] = line.split(" = ")
        [linkL, linkR] = links.split(', ')
        linkL = linkL[1:]
        linkR = linkR[:-1]
        nodes[node] = {"L":linkL, "R":linkR}

        if node[-1] == 'A':
            startingNodes.append(node)

    return (raw[0], nodes, startingNodes)

def solution(inputFile):

    (directions, nodes, locations) = getInputData(inputFile)

    stepCycles = []

    for location in locations:
        stepCounter = 0
        matches = 10
        while(matches>0):
            location = nodes[location][directions[stepCounter%len(directions)]]
            stepCounter+=1

            if location[-1] == 'Z':
                stepCycles.append(stepCounter)
                break

    finalPrimeDivisors = {}
    for stepCycle in stepCycles:
        primeDivisors = numberUtils.splitIntoPrimeDivisorsPow(stepCycle)
        for pDiv in primeDivisors:
            if not pDiv in finalPrimeDivisors:
                finalPrimeDivisors[pDiv] = primeDivisors[pDiv]
            else:
                finalPrimeDivisors[pDiv] = max(finalPrimeDivisors[pDiv],primeDivisors[pDiv])

    result = 1
    for pDiv in finalPrimeDivisors:
        result *= pow(pDiv, finalPrimeDivisors[pDiv])

    # log(red())

    return (result, EXPECTED_RESULT)