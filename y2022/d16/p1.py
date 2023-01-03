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
        phase2[entry[0]] = {"flowRate":entry[1], "tunnelsTo":entry[2]}

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

def chooseNextValve(totalFlow, flowRate, currentValve, elapsedMinutes, openValves, relevantValves, valve1ToValve2Distances, flowRates):
    maxFlow = 0
    for tuple in [tuple for tuple in valve1ToValve2Distances if tuple[0]==currentValve and not tuple[1] in openValves]:
        newElapsedMinutes = elapsedMinutes + tuple[2] + 1
        newTotalFlow = totalFlow + flowRate*(tuple[2] + 1)

        if newElapsedMinutes<=MINUTES_LIMIT:
            maxFlow = max(maxFlow,chooseNextValve(newTotalFlow, flowRate + flowRates[tuple[1]], tuple[1], newElapsedMinutes, openValves+[tuple[1]], relevantValves, valve1ToValve2Distances, flowRates))
        else:
            # out of time
            break

    maxFlow = max(maxFlow, totalFlow + flowRate*(MINUTES_LIMIT - elapsedMinutes))

    return maxFlow
        

def solution(inputFile):
    valves = getInputData(inputFile)
    relevantValves = [valve for valve in valves if valves[valve]["flowRate"]>0]

    valve1ToValve2Distances = []
    valveAAToValveDistances = {}
    flowRates = {}

    for relevantValve in relevantValves:
        valveAAToValveDistances[relevantValve] = getDistance('AA', relevantValve, valves)
        flowRates[relevantValve] = valves[relevantValve]["flowRate"]

    for valveIndexA in range(len(relevantValves)-1):
        for valveIndexB in range(valveIndexA+1, len(relevantValves)):
            valveA = relevantValves[valveIndexA]
            valveB = relevantValves[valveIndexB]

            dist = getDistance(valveA, valveB, valves)
            valve1ToValve2Distances.append((valveA,valveB,dist))
            valve1ToValve2Distances.append((valveB,valveA,dist))

    valve1ToValve2Distances.sort(key=lambda e:e[2])

    maxFlow = 0
    for relevantValve in relevantValves:
        elapsedMinutes = valveAAToValveDistances[relevantValve]+1

        maxFlow = max(maxFlow, chooseNextValve(0, flowRates[relevantValve], relevantValve, elapsedMinutes, [relevantValve], relevantValves, valve1ToValve2Distances, flowRates))

    return maxFlow