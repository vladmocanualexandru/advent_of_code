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

from functools import cmp_to_key
 
EXPECTED_RESULT = None
WRONG_RESULTS = [2628, 2627]
DEFAULT_TENT_DIST = pow(10,5)

def compareCoords(c1,c2):
    if c1[0]!=c2[0]:
        return c1[0]-c2[0]
    elif c1[1]!=c2[1]:
        return c1[1]-c2[1]
    else:
        return c1[2]-c2[2]

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, ',')
    
    processed=[(entry[0],entry[1],entry[2]) for entry in raw]

    return processed 

def getUnreachableNodes(source, graph):
    unvisited = []

    for nodeLabel in graph:
        graph[nodeLabel]["tentDist"] = DEFAULT_TENT_DIST
        unvisited.append(nodeLabel)

    graph[source]["tentDist"] = 0

    while len(unvisited)>0:
        unvisited.sort(key=lambda e:graph[e]["tentDist"])

        currentNode = unvisited[0]

        # if the smallest tentative distance is default value -> remaining nodes are unreachable
        if graph[currentNode]["tentDist"] == DEFAULT_TENT_DIST:
            return unvisited

        for connection in graph[currentNode]["connections"]:
            if connection in unvisited:
                graph[connection]["tentDist"] = min(graph[connection]["tentDist"], graph[currentNode]["tentDist"]+1)

        unvisited.remove(currentNode)

    return []
    
def generateCubeLabel(x,y,z):
    return "%d_%d_%d" % (x,y,z)

def solution(inputFile):
    solidCubes = getInputData(inputFile)

    # calculate space dimensions based on min/max of inpute data solidCubes' x,y,z coordinates
    minX = minY = minZ = pow(10,3)
    maxX = maxY = maxZ = -pow(10,3)

    for (x,y,z) in solidCubes:
        minX = min(minX, x)
        minY = min(minY, y)
        minZ = min(minX, z)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        maxZ = max(maxZ, z)

    # translate all solidCubes to 0,0,0 (+1 to leave room for the 1cube wide padding layer)
    solidCubes = [(x-minX+1,y-minY+1,z-minZ+1) for (x,y,z) in solidCubes]
    maxX=maxX-minX+1
    maxY=maxY-minY+1
    maxZ=maxZ-minZ+1

    # +2 (to allow layer of free cube padding)
    spaceWidth = maxX+2
    spaceHeight = maxY+2
    spaceDepth = maxZ+2

    log("spaceWidth",spaceWidth)
    log("spaceHeight",spaceHeight)
    log("spaceDepth",spaceDepth)

    # generating free cubes
    freeCubes = []
    for x in range(spaceWidth):
        for y in range(spaceHeight):
            for z in range(spaceDepth):
                freeCubes.append((x,y,z))

    # iterating through input cubes, and removing from free cubes
    for cube in solidCubes:
        freeCubes.remove(cube)

    # generate 3d graph of the remaining freeCubes
    freeCubeGraph = {}
    for (x,y,z) in freeCubes:
        cubeNode = {"connections":[]}
        freeCubeGraph[generateCubeLabel(x,y,z)] = cubeNode

        if x > 0 and (x-1,y,z) in freeCubes:
            cubeNode["connections"].append(generateCubeLabel(x-1,y,z))
        if x < spaceWidth-1 and (x+1,y,z) in freeCubes:
            cubeNode["connections"].append(generateCubeLabel(x+1,y,z))
        if y > 0 and (x,y-1,z) in freeCubes:
            cubeNode["connections"].append(generateCubeLabel(x,y-1,z))
        if y < spaceHeight-1 and (x,y+1,z) in freeCubes:
            cubeNode["connections"].append(generateCubeLabel(x,y+1,z))
        if z > 0 and (x,y,z-1) in freeCubes:
            cubeNode["connections"].append(generateCubeLabel(x,y,z-1))
        if z < spaceDepth-1 and (x,y,z+1) in freeCubes:
            cubeNode["connections"].append(generateCubeLabel(x,y,z+1))
      
    unreachableNodes = getUnreachableNodes("0_0_21", freeCubeGraph)
    # log(unreachableNodes)
    log(len(unreachableNodes))

    result = 0

    if len(WRONG_RESULTS)>0:
        log(red("Wrong results", WRONG_RESULTS))

    return (result,EXPECTED_RESULT)