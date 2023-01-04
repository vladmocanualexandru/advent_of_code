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
MINUTES_LIMIT = 26

relevantValves = []
valve1ToValve2Distances = []
flowRates={}

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

def solution(inputFile):
    valves = getInputData(inputFile)
    relevantValves = [valve for valve in valves if valves[valve]["flowRate"]>0]

    valveAAToValveDistances = {}    

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

    # init stateCollection
    stateCollection = []

    # for valveIndexA in range(len(relevantValves)-1):
        # for valveIndexB in range(valveIndexA+1, len(relevantValves)):
    valveIndexA = 0 
    valveIndexB = 1 
    
    valveA = relevantValves[valveIndexA]
    valveB = relevantValves[valveIndexB]

    # elapsedMinutesA, elapsedMinutesB, totalFlowA, totalFlowB, flowRateA, flowRateB, currentValveA, currentValveB, openValves
    elapsedMinutesA = valveAAToValveDistances[valveA]+1
    elapsedMinutesB = valveAAToValveDistances[valveB]+1
    flowRateA = flowRates[valveA]
    flowRateB = flowRates[valveB]
    openValves = [valveA, valveB]

    stateCollection.append((elapsedMinutesA, elapsedMinutesB, 0, 0, flowRateA, flowRateB, valveA, valveB, openValves))

    knownStates = []

    maxTotalFlowRate = 0
    while len(stateCollection)>0:
        # queue <-> BFS
        # currentState = stateCollection.pop(0)

        # queue <-> DFS
        currentState = stateCollection.pop(-1)

        knownStates.append(currentState)

        (elapsedMinutesA, elapsedMinutesB, totalFlowA, totalFlowB, flowRateA, flowRateB, currentValveA, currentValveB, openValves) = currentState

        noMoreValves = False
        newMoveGenerated = False
        for tupleA in [tuple for tuple in valve1ToValve2Distances if tuple[0]==currentValveA and not tuple[1] in openValves]:
            for tupleB in [tuple for tuple in valve1ToValve2Distances if tuple[0]==currentValveB and not tuple[1] in openValves]:
                if tupleA[1] != tupleB[1]:
                    newMoveGenerated = True

                    newElapsedMinutesA = elapsedMinutesA + tupleA[2] + 1
                    newElapsedMinutesB = elapsedMinutesB + tupleB[2] + 1

                    if newElapsedMinutesA>MINUTES_LIMIT and newElapsedMinutesB>MINUTES_LIMIT:
                        noMoreValves = True
                        break

                    newTotalFlowA = totalFlowA
                    newTotalFlowB = totalFlowB

                    newFlowRateA = flowRateA
                    newFlowRateB = flowRateB

                    newCurrentValveA = currentValveA
                    newCurrentValveB = currentValveB
                    
                    newOpenValves = openValves.copy()

                    if newElapsedMinutesA<=MINUTES_LIMIT:
                        newTotalFlowA += flowRateA*(tupleA[2] + 1)
                        newFlowRateA += flowRates[tupleA[1]]
                        newCurrentValveA = tupleA[1]
                        newOpenValves.append(newCurrentValveA)
                    else:
                        newElapsedMinutesA = elapsedMinutesA

                    if newElapsedMinutesB<=MINUTES_LIMIT:
                        newTotalFlowB += flowRateB*(tupleB[2] + 1)
                        newFlowRateB += flowRates[tupleB[1]]
                        newCurrentValveB = tupleB[1]
                        newOpenValves.append(newCurrentValveB)
                    else:
                        newElapsedMinutesB = elapsedMinutesB

                    newOpenValves.sort()
                    state = (newElapsedMinutesA, newElapsedMinutesB, newTotalFlowA, newTotalFlowB, newFlowRateA, newFlowRateB, newCurrentValveA, newCurrentValveB, newOpenValves)
                    
                    if not state in knownStates:
                        stateCollection.append(state)
        
            if noMoreValves:
                currentTotalFlow = totalFlowA + flowRateA*(MINUTES_LIMIT - elapsedMinutesA)
                currentTotalFlow += totalFlowB + flowRateB*(MINUTES_LIMIT - elapsedMinutesB)
                
                maxTotalFlowRate = max(maxTotalFlowRate, currentTotalFlow)
                # log(maxTotalFlowRate)
                break

        if not newMoveGenerated:
            currentTotalFlow = totalFlowA + flowRateA*(MINUTES_LIMIT - elapsedMinutesA)
            currentTotalFlow += totalFlowB + flowRateB*(MINUTES_LIMIT - elapsedMinutesB)
            
            maxTotalFlowRate = max(maxTotalFlowRate, currentTotalFlow)
            # log(maxTotalFlowRate)

    return maxTotalFlowRate