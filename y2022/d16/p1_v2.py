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
 
TOP_VALVES = 8

DEFAULT_TENT_DISTANCE = pow(10,10)
MINUTES_LIMIT = 30


# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
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

    closedValves.sort(key=lambda e: valves[e]["flowRate"], reverse=True)

    closedValves = closedValves[:TOP_VALVES]

    maxTotalFlow = 0
    maxTotalFlowRoute = []

    permutations = permutation(closedValves)
    for valveArrangement in permutations:
        log("%d%%" % round(permutations.index(valveArrangement)/len(permutations)*100))

        currentValve = "AA"
        spentMinutes = 0
        flowPerMin = 0
        totalFlow = 0
        for valveLabel in valveArrangement:
            dist=getRouteLength(currentValve, valveLabel, valves)
            if spentMinutes+dist+1>MINUTES_LIMIT:
                # log("ran out of time @ valve", valveLabel, "flow",totalFlow)
                break

            totalFlow+=flowPerMin*(dist+1)
            flowPerMin+=valves[valveLabel]["flowRate"]
            spentMinutes+=dist+1
            currentValve = valveLabel
        else:
            totalFlow+=flowPerMin*(MINUTES_LIMIT-spentMinutes)
            # log("ran out of valves; spent time", spentMinutes, "flow",totalFlow)

        if totalFlow>maxTotalFlow:
            log(purple("found better", totalFlow))
            maxTotalFlow = totalFlow
            maxTotalFlowRoute = valveArrangement
            

    log("best arrangement", maxTotalFlow, maxTotalFlowRoute)

    # currentValve = "AA"
    # spentMinutes = 0

    # flowPerMin = 0
    # totalFlow = 0
    # while len(closedValves) > 0 and spentMinutes < MINUTES_LIMIT:

    #     for closedValve1 in closedValves:
    #         valve1 = valves[closedValve1]
    #         valve1["proximityValue"] = 1
    #         for closedValve2 in closedValves:
    #             valve2 = valves[closedValve2]
    #             if closedValve1 != closedValve2 and valve2["flowRate"] > valve1["flowRate"] and getRouteLength(closedValve1,closedValve2,valves)<PROXIMITY_VALUE_DISTANCE:
    #                 valve1["proximityValue"]+=1

    #     nodeAnalysis = []
    #     for closedValve in closedValves:
    #         dist = getRouteLength(currentValve, closedValve, valves)
    #         flowDistRatio = round(valves[closedValve]["flowRate"]/dist+0.00000000000001) + PROXIMITY_VALUE_IMPORTANCE*(valves[closedValve]["proximityValue"])
    #         nodeAnalysis.append((closedValve, dist, flowDistRatio,valves[closedValve]["flowRate"]))

    #     nodeAnalysis.sort(key=cmp_to_key(compareAnalysisItem))

    #     # log(currentValve, nodeAnalysis)

    #     for analysisItem in nodeAnalysis:
    #         if (analysisItem[1]+spentMinutes+1)<=MINUTES_LIMIT:
    #             currentValve = analysisItem[0]
    #             spentMinutes += analysisItem[1]+1
    #             totalFlow += flowPerMin*(analysisItem[1]+1)
    #             flowPerMin += analysisItem[3] 
    #             closedValves.remove(currentValve)

    #             log(currentValve, valves[currentValve])
    #             break
    #     else:
    #         break

    # log("Finished in", spentMinutes)

    # if (spentMinutes>0):
    #     totalFlow += (MINUTES_LIMIT-spentMinutes)*flowPerMin
    # # log(spentMinutes)

    log(red(1417, 1602, 1721, 1981, 1966, 1953))
    return None