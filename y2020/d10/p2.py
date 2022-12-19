import itertools, sys, os, math
from itertools import compress

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 15790581481472

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)

    raw.sort()

    processed=[0]+raw+[raw[-1]+3]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample', inputData[:20])

    graph = {}

    for i in range(len(inputData)):
        nodeFrom = inputData[i]
        graph[nodeFrom] = {"connectedTo":[], "value":0}

        for j in range(i+1,len(inputData)):
            nodeTo = inputData[j]
            if nodeTo<=nodeFrom+3:
                graph[nodeFrom]["connectedTo"].append(nodeTo)
            else:
                break

    graph[0]["value"]=1
    for nodeLabel in graph:
        node = graph[nodeLabel]

        for child in node["connectedTo"]:
            graph[child]["value"]+=node["value"]


    # log(graph)

    result = graph[inputData[-1]]["value"]
    return (result, EXPECTED_RESULT)

 
