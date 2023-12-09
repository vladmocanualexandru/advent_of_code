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

EXPECTED_RESULT = 16343
 
def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[entry for entry in raw[2:]]
    nodes = {}
    for line in processed:
        [node, links] = line.split(" = ")
        [linkL, linkR] = links.split(', ')
        linkL = linkL[1:]
        linkR = linkR[:-1]
        nodes[node] = {"L":linkL, "R":linkR}

    return (raw[0], nodes)

def solution(inputFile):
    (directions, nodes) = getInputData(inputFile)

    stepCounter = 0
    location = 'AAA'
    while (location!='ZZZ'):
        location = nodes[location][directions[stepCounter%len(directions)]]
        stepCounter+=1

    result = stepCounter

    # log(red())
    return (result, EXPECTED_RESULT)