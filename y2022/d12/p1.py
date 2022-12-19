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
 
EXPECTED_RESULT = 394
DEFAULT_TENT_DIST = pow(10,5)

def generateNode(id, value):
    node = {
        "id": id,
        "isStart": False,
        "isStop": False,
        "value": value-97,
        "connections": [],
        "tentDist": DEFAULT_TENT_DIST
    }

    if node["value"] == -14:
        node["value"] = 0
        node["isStart"] = True
    elif node["value"] == -28:
        node["value"] = 25
        node["isStop"] = True

    return node

def getInputData(inputFile):
    # read from file
    phase1 = getTuples_text(inputFile,'')
    
    # convert to values
    phase2=[[ord(c) for c in entry] for entry in phase1]

    # generate nodes + search for start and stop
    phase3 = []
    start = stop = None
    for li in range(len(phase2)):
        line = []
        for ci in range(len(phase2[li])):
            id = "%d_%d" % (li, ci)
            node = generateNode(id, phase2[li][ci])

            if node["isStart"]:
                start = id
            elif node["isStop"]:
                stop = id

            line.append(node)

        phase3.append(line)

    # generate connections
    phase4 = {}
    for li in range(len(phase3)):
        for ci in range(len(phase3[li])):
            currentNode = phase3[li][ci]
            
            for (node,coords) in matrixUtils.getNeighbors4(phase3, li, ci, includeNeighborCoords=True):

                if currentNode["value"]-node["value"]>=-1:
                    currentNode["connections"].append(node["id"])

            phase4[currentNode["id"]] = currentNode
    # uncomment for nice visual
    # return (phase4, start, stop, phase2)
    return (phase4, start, stop)

def solution(inputFile):
    # uncomment for nice visual
    # (nodes, start, stop, map) = getInputData(inputFile)
    (nodes, start, stop) = getInputData(inputFile)
    
    nodes[start]["tentDist"]  = 0

    unvisitedNodes = [id for id in nodes]
    
    unvisitedNodes.sort(key=lambda e: nodes[e]["tentDist"])

    result=None
    while len(unvisitedNodes) > 0 and nodes[unvisitedNodes[0]]["tentDist"]<DEFAULT_TENT_DIST:
        currentNode = nodes[unvisitedNodes[0]]

        if currentNode["isStop"]:
            result = currentNode["tentDist"]
            break

        for connection in currentNode["connections"]:
            if connection in unvisitedNodes:
                newTentDist = currentNode["tentDist"]+1

                if newTentDist<nodes[connection]["tentDist"]:
                    nodes[connection]["tentDist"] = newTentDist

        unvisitedNodes.remove(currentNode["id"])

        unvisitedNodes.sort(key=lambda e: nodes[e]["tentDist"])

    # uncomment for nice visual
    # currentNode = stop
    # while currentNode != start:
    #     revNeighbors = [nodes[id] for id in nodes if currentNode in nodes[id]["connections"]]
    #     revNeighbors.sort(key=lambda e: e["tentDist"])
    #     currentNode = revNeighbors[0]["id"]

    #     if currentNode!=start:
    #         coords = currentNode.split("_")
    #         map[int(coords[0])][int(coords[1])] = 0

    # matrixUtils.log(map, '', log, lambda e: purple(C_BLOCK) if e==0 else purple(C_DOT_FULL) if e < 97 else blue(C_BLOCK) if e < 98 else  green(C_BLOCK) if e<105 else yellow(C_BLOCK) if e<119 else red(C_BLOCK))

    return (result,EXPECTED_RESULT)