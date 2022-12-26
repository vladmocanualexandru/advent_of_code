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
PROXIMITY_VALUE_IMPORTANCE=1
PROXIMITY_VALUE_DISTANCE=3

def getInputData(inputFile):
    raw = getTuples_text(inputFile, " has flow rate=", "; tunnel", " to ", ", ", "Valve ")
    
    phase1=[(entry[1], int(entry[2]), [innerEntry.replace("valves ","").replace("valve ","") for innerEntry in entry[4:]]) for entry in raw]

    phase2 = {}
    for entry in phase1:
        phase2[entry[0]] = {"flowRate":entry[1], "tunnelsTo":entry[2], "proximityValue":0}

    return phase2 

def getRouteLength(start, stop, valves):
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

def compareAnalysisItem(ai1, ai2):
    if ai1[2]!=ai2[2]:
        return ai2[2]-ai1[2]
    else:
        return ai1[1]-ai2[1]

def solution(inputFile):
    valves = getInputData(inputFile)
    closedValves = [valveLabel for valveLabel in valves if valves[valveLabel]["flowRate"]>0]

    currentValve = "AA"
    spentMinutes = 0

    flowPerMin = 0
    totalFlow = 0
    while len(closedValves) > 0 and spentMinutes < MINUTES_LIMIT:

        for closedValve1 in closedValves:
            valve1 = valves[closedValve1]
            valve1["proximityValue"] = 1
            for closedValve2 in closedValves:
                valve2 = valves[closedValve2]
                if closedValve1 != closedValve2 and valve2["flowRate"] > valve1["flowRate"] and getRouteLength(closedValve1,closedValve2,valves)<PROXIMITY_VALUE_DISTANCE:
                    valve1["proximityValue"]+=1

        nodeAnalysis = []
        for closedValve in closedValves:
            dist = getRouteLength(currentValve, closedValve, valves)
            flowDistRatio = round(valves[closedValve]["flowRate"]/dist+0.00000000000001) + PROXIMITY_VALUE_IMPORTANCE*(valves[closedValve]["proximityValue"])
            nodeAnalysis.append((closedValve, dist, flowDistRatio,valves[closedValve]["flowRate"]))

        nodeAnalysis.sort(key=cmp_to_key(compareAnalysisItem))

        # log(currentValve, nodeAnalysis)

        for analysisItem in nodeAnalysis:
            if (analysisItem[1]+spentMinutes+1)<=MINUTES_LIMIT:
                currentValve = analysisItem[0]
                spentMinutes += analysisItem[1]+1
                totalFlow += flowPerMin*(analysisItem[1]+1)
                flowPerMin += analysisItem[3] 
                closedValves.remove(currentValve)

                log(currentValve, valves[currentValve])
                break
        else:
            break

    log("Finished in", spentMinutes)

    if (spentMinutes>0):
        totalFlow += (MINUTES_LIMIT-spentMinutes)*flowPerMin
    # log(spentMinutes)

    log(red(1417, 1602, 1721, 1981, 1966))
    return totalFlow