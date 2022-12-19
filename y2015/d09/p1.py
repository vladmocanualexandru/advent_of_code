from concurrent.futures import process
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 117

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' = ', ' to ')
    
    processed=[]

    for entry in raw:
        processed.append((entry[0], entry[1], int(entry[2])))
        processed.append((entry[1], entry[0], int(entry[2])))

    return processed 

def computeRoutes(currentLocation, route, distance, connections, resultCollector):
    localRoute = route + []

    localRoute.append(currentLocation)

    endOfRoute = True
    for nextLocation in connections[currentLocation]["destinations"]:
        if not nextLocation[0] in localRoute:
            endOfRoute = False
            computeRoutes(nextLocation[0], localRoute, distance + nextLocation[1], connections, resultCollector)

    if endOfRoute:
        resultCollector.append((localRoute, distance))

    if route == []:
        return resultCollector


def solution(inputFile):
    inputData = getInputData(inputFile)
    # # log('input sample', inputData[:10])

    connections = {}

    for entry in inputData:
        if not entry[0] in connections:
            connections[entry[0]] = {"destinations":[]}

        connections[entry[0]]["destinations"].append((entry[1], entry[2]))

    # log(connections)

    routes = []
    for connection in connections:
        routes = routes+computeRoutes(connection, [], 0, connections, [])

    routes.sort(key=lambda e: e[1])

    result=routes[0][-1]
    
    return (result, EXPECTED_RESULT)

 

