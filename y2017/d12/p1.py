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
 
EXPECTED_RESULT = 115

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, ' <-> ', ', ')
    
    processed=[entry[1:] for entry in raw]

    return processed 

def canReach0(nodes, currentNode, visitedNodes):
    visitedNodes.append(currentNode)
    # log(visitedNodes)

    for nextNode in nodes[currentNode]:
        if nextNode == 0:
            return True
        if not nextNode in visitedNodes:
            innerResult = canReach0(nodes, nextNode, visitedNodes)
            if innerResult:
                return True

    visitedNodes.remove(currentNode)
    return False

    

def solution(inputFile):
    pipes = getInputData(inputFile)

    result=0
    for nodeIndex in range(len(pipes)):
        if canReach0(pipes, nodeIndex, []):
            result+=1

    return (result,EXPECTED_RESULT)