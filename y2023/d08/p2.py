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

    # pasul 1: obtin dimensiunea ciclului fiecarei locatii
    # pasul 2: cu 6 numere, se calculeaza cel mai mic multiplu comun
    # pasul 3: profit!

    stepCounters = [0 for i in range(len(locations))]
    stepCombinations = [[] for i in range(len(locations))]
    repetitionFound = [False for i in range(len(locations))]

    resultFound = False
    maxSteps = -1
    while(not resultFound):
        for locationIndex in range(len(locations)):
            location = locations[locationIndex]
            stepCounter = stepCounters[locationIndex]
            while (stepCounter != maxSteps):
                location = nodes[location][directions[stepCounters[locationIndex]%len(directions)]]
                stepCounters[locationIndex]+=1

                if location[-1]=='Z':
                    combination = (location, stepCounters[locationIndex]%len(directions))
                    if combination in stepCombinations[locationIndex]:
                        log(green("Repetition found!", locationIndex, location, stepCounters[locationIndex]))
                        repetitionFound[locationIndex] = True
                    else:
                        stepCombinations[locationIndex].append(combination)

                    break

            locations[locationIndex] = location

        if repetitionFound == [True for i in range(len(locations))]:
            break

        
        resultFound = True
        result = stepCounters[0]
        for stepCounter in stepCounters[1:]:
            if result!=stepCounter:
                maxSteps = max(stepCounters)
                log("max steps", maxSteps)
                resultFound = False
                break

    # log(red())
    return (result, EXPECTED_RESULT)