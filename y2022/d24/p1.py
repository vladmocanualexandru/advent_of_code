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
 
DIRECTIONS = {">":(0,1),"v":(1,0),"<":(0,-1),"^":(-1,0)}

def vizualizeMap(map, storms):

    cloneMap = matrixUtils.clone(map)
    for storm in storms:
        (stormY, stormX) = (storm["location"][0], storm["location"][1])
        if cloneMap[stormY][stormX] == '.':
            cloneMap[stormY][stormX] = storm["type"]
        elif cloneMap[stormY][stormX] in DIRECTIONS:
            cloneMap[stormY][stormX] = 2
        else:
            cloneMap[stormY][stormX] += 1

    logMatrix(cloneMap)

def moveStorm(storm, portals):
    location = storm["location"]
    directionData = DIRECTIONS[storm["type"]]

    location[0] = location[0] + directionData[0]
    location[1] = location[1] + directionData[1]

    if (location[0],location[1]) in portals:
        newLocation = portals[(location[0],location[1])]

        location[0] = newLocation[0]
        location[1] = newLocation[1]

def getInputData(inputFile):
    originalMap = getTuples_text(inputFile,'')

    map = matrixUtils.generate(len(originalMap), len(originalMap[0]), '.')
    
    storms = []
    portals = {}
    for lineIndex in range(len(originalMap)):
        for colIndex in range(len(originalMap[0])):
            mapChar = originalMap[lineIndex][colIndex]
            if mapChar in ['>','v','<','^']:
                storms.append({"type":mapChar, "location":[lineIndex, colIndex]})
            elif mapChar == '#':
                map[lineIndex][colIndex] = '#'
                if lineIndex==0:
                    portals[(lineIndex,colIndex)] = (len(originalMap)-2, colIndex)
                elif lineIndex == len(originalMap)-1:
                    portals[(lineIndex,colIndex)] = (1, colIndex)
                elif colIndex == 0:
                    portals[(lineIndex,colIndex)] = (lineIndex, len(originalMap[0])-2)
                elif colIndex == len(originalMap[0])-1:
                    portals[(lineIndex,colIndex)] = (lineIndex, 1)
                # else:
                #     # normal positions are portals to themselves - might be an optimization point
                #     portals[(lineIndex,colIndex)] = (lineIndex, colIndex)

    return (map, storms, portals)

def solution(inputFile):
    (map, storms, portals) = getInputData(inputFile)

    height = len(map)
    width = len(map[0])

    myY,myX = (0,1) 
    destinationY,destinationX = (height-1,width-2) 

    minuteCounter = 0

    vizualizeMap(map.copy(), storms)
    time.sleep(1)

    while minuteCounter<3600:
        # move storms
        for storm in storms:
            moveStorm(storm, portals)

        minuteCounter+=1

        if minuteCounter%12 == 0:
            log(minuteCounter)
            vizualizeMap(map, storms)
            time.sleep(1)



    return None