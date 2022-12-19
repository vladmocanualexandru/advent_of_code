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
 
EXPECTED_RESULT = 221

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, ' <-> ', ', ')
    
    processed=[entry[1:] for entry in raw]

    return processed 

def canReachTarget(target, nodes, currentNode, visitedNodes):
    visitedNodes.append(currentNode)
    # log(visitedNodes)

    for nextNode in nodes[currentNode]:
        if nextNode == target:
            return True
        if not nextNode in visitedNodes:
            innerResult = canReachTarget(target, nodes, nextNode, visitedNodes)
            if innerResult:
                return True

    visitedNodes.remove(currentNode)
    return False

    

def solution(inputFile):
    pipes = getInputData(inputFile)

    result=0
    visited = []
    while len(visited)<len(pipes):
        # find new target
        for target in range(len(pipes)):
            if not target in visited:
                groupFound = False
                for nodeIndex in range(len(pipes)):
                    if not nodeIndex in visited and canReachTarget(target, pipes, nodeIndex, []):
                        visited.append(nodeIndex)

                        if not groupFound:
                            groupFound=True
                            result+=1
                break

    return (result,EXPECTED_RESULT)