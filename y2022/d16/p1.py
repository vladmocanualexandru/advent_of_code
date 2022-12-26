import sys, os, math
import numpy as np
import pandas as pd

from functools import cmp_to_key

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
DEFAULT_TENT_DISTANCE = pow(10,10)
MINUTES_LIMIT = 30

def getInputData(inputFile):
    raw = getTuples_text(inputFile, " has flow rate=", "; tunnel", " to ", ", ", "Valve ")
    
    phase1=[(entry[1], int(entry[2]), [innerEntry.replace("valves ","").replace("valve ","") for innerEntry in entry[4:]]) for entry in raw]

    phase2 = {}
    for entry in phase1:
        phase2[entry[0]] = {"flowRate":entry[1], "tunnelsTo":entry[2], "proximityValue":0}

    return phase2 

def getDistance(start, stop, valves):
    unvisited = [valveLabel for valveLabel in valves]
    for valveLabel in valves:
        valves[valveLabel]["tentDistance"] = DEFAULT_TENT_DISTANCE

    valves[start]["tentDistance"] = 0

    unvisited.sort(key=lambda e: valves[e]["tentDistance"])
    while len(unvisited) > 0 and valves[unvisited[0]]["tentDistance"] < DEFAULT_TENT_DISTANCE:
        currentValve = unvisited[0]
        for connection in valves[currentValve]["tunnelsTo"]:
            valves[connection]["tentDistance"] = min(valves[currentValve]["tentDistance"]+1, valves[connection]["tentDistance"])

        if currentValve == stop:
            return valves[currentValve]["tentDistance"]
        else:
            unvisited.remove(currentValve)
            unvisited.sort(key=lambda e: valves[e]["tentDistance"])

    return None

def compareOptions(o1,o2):
    if o1["loss"] != o2["loss"]:
        return o1["loss"]-o2["loss"]
    else:
        return o2["flowRate"]-o1["flowRate"]

def solution(inputFile):
    valves = getInputData(inputFile)

    relevantValves = [valveLabel for valveLabel in valves if valves[valveLabel]["flowRate"]>0]

    # log("totalFlowPotential", totalFlowPotential)

    for relevantValve in relevantValves:
        dist = getDistance("AA", relevantValve, valves)
        potentialValue = (MINUTES_LIMIT*valves[relevantValve]["flowRate"])
        realValue = ((MINUTES_LIMIT-dist-1)*valves[relevantValve]["flowRate"])
        log("AA ->", relevantValve, "dist=", dist, "potential=", (MINUTES_LIMIT*valves[relevantValve]["flowRate"]),"real=",realValue)

    # log(totalFlowPotential)

    log(red(1417, 1602, 1721, 1981, 1966, 1953, 2030, 2110))

    return None