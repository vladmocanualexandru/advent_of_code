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
 
EXPECTED_RESULT = 388
DEFAULT_TENT_DIST = pow(10,5)

def generateNode(id, value):
    node = {
        "id": id,
        "isStart": False,
        "value": value-97,
        "connections": [],
        "tentDist": DEFAULT_TENT_DIST
    }

    if node["value"] == -14:
        node["value"] = 0
    elif node["value"] == -28:
        node["value"] = 25
        node["isStart"] = True

    return node

def getInputData(inputFile):
    # read from file
    phase1 = getTuples_text(inputFile,'')
    
    # convert to values
    phase2=[[ord(c) for c in entry] for entry in phase1]

    # generate nodes + search for start and stop
    phase3 = []
    start = None
    for li in range(len(phase2)):
        line = []
        for ci in range(len(phase2[li])):
            id = "%d_%d" % (li, ci)
            node = generateNode(id, phase2[li][ci])

            if node["isStart"]:
                start = id

            line.append(node)

        phase3.append(line)

    # generate connections
    phase4 = {}
    for li in range(len(phase3)):
        for ci in range(len(phase3[li])):
            currentNode = phase3[li][ci]
            
            for (node,coords) in matrixUtils.getNeighbors4(phase3, li, ci, includeNeighborCoords=True):

                if currentNode["value"]-node["value"]<=1:
                    currentNode["connections"].append(node["id"])

            phase4[currentNode["id"]] = currentNode

    return (phase4, start)

def solution(inputFile):
    (nodes, start) = getInputData(inputFile)
    
    result = DEFAULT_TENT_DIST


    nodes[start]["tentDist"]  = 0

    unvisitedNodes = [id for id in nodes]
    
    unvisitedNodes.sort(key=lambda e: nodes[e]["tentDist"])

    result = None
    while len(unvisitedNodes) > 0 and nodes[unvisitedNodes[0]]["tentDist"]<DEFAULT_TENT_DIST:
        currentNode = nodes[unvisitedNodes[0]]

        if currentNode["value"] == 0:
            result = currentNode["tentDist"]
            break

        for connection in currentNode["connections"]:
            if connection in unvisitedNodes:
                newTentDist = currentNode["tentDist"]+1

                if newTentDist<nodes[connection]["tentDist"]:
                    nodes[connection]["tentDist"] = newTentDist

        unvisitedNodes.remove(currentNode["id"])

        unvisitedNodes.sort(key=lambda e: nodes[e]["tentDist"])

    return (result,EXPECTED_RESULT)