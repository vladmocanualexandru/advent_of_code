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

def calculateMaxFlow(elapsedMinutesE, elapsedMinutesP, totalFlowE, totalFlowP, flowRateE, flowRateP, currentValveE, currentValveP,  openValves):

    maxFlow = 0

    noMoreValves = False
    for tupleE in [tuple for tuple in valve1ToValve2Distances if tuple[0]==currentValveE and not tuple[1] in openValves]:
        for tupleP in [tuple for tuple in valve1ToValve2Distances if tuple[0]==currentValveP and not tuple[1] in openValves]:
            if tupleE[1] != tupleP[1]:
                # log(openValvesE, openValvesP, tupleE, tupleP)
                newElapsedMinutesE = elapsedMinutesE + tupleE[2] + 1
                newElapsedMinutesP = elapsedMinutesP + tupleP[2] + 1

                if newElapsedMinutesE>MINUTES_LIMIT and newElapsedMinutesP>MINUTES_LIMIT:
                    noMoreValves = True
                    break

                newTotalFlowE = totalFlowE
                newTotalFlowP = totalFlowP

                newFlowRateE = flowRateE
                newFlowRateP = flowRateP

                newCurrentValveE = currentValveE
                newCurrentValveP = currentValveP
                
                newOpenValves = openValves.copy()

                if newElapsedMinutesE<=MINUTES_LIMIT:
                    newTotalFlowE += flowRateE*(tupleE[2] + 1)
                    newFlowRateE += flowRates[tupleE[1]]
                    newCurrentValveE = tupleE[1]
                    newOpenValves.append(newCurrentValveE)
                else:
                    newElapsedMinutesE = elapsedMinutesE

                if newElapsedMinutesP<=MINUTES_LIMIT:
                    newTotalFlowP += flowRateP*(tupleP[2] + 1)
                    newFlowRateP += flowRates[tupleP[1]]
                    newCurrentValveP = tupleP[1]
                    newOpenValves.append(newCurrentValveP)
                else:
                    newElapsedMinutesP = elapsedMinutesP

                maxFlow = max(maxFlow, calculateMaxFlow(newElapsedMinutesE, newElapsedMinutesP, newTotalFlowE, newTotalFlowP, newFlowRateE, newFlowRateP, newCurrentValveE, newCurrentValveP,  newOpenValves))
        
        if noMoreValves:
            break

    totalFlow = totalFlowE + flowRateE*(MINUTES_LIMIT - elapsedMinutesE)
    totalFlow += totalFlowP + flowRateP*(MINUTES_LIMIT - elapsedMinutesP)

    return max(maxFlow, totalFlow)

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

    maxFlow = 0
    for valveEIndex in range(len(relevantValves)-1):
        for valvePIndex in range(valveEIndex+1, len(relevantValves)):
            log(valveEIndex, valvePIndex)

            valveE = relevantValves[valveEIndex]
            valveP = relevantValves[valvePIndex]

            elapsedMinutesE = valveAAToValveDistances[valveE]+1
            elapsedMinutesP = valveAAToValveDistances[valveP]+1

            maxFlow = max(maxFlow, calculateMaxFlow(elapsedMinutesE, elapsedMinutesP, 0, 0, flowRates[valveE], flowRates[valveP], valveE, valveP, [valveE, valveP]))
        
    return maxFlow