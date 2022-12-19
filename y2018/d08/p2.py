from array import array
from platform import node
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 16653

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile)
    
    processed=raw[0]

    return processed 

def calculateNodeValue(label, nodes):
    node = nodes[label]

    if node["children"] == []:
        node["value"] = sum(node["metadata"])
    else:
        for child in node["children"]:
            calculateNodeValue(child, nodes)
        
        node["value"] = sum([nodes[node["children"][metaInd-1]]["value"] for metaInd in node["metadata"] if metaInd in range(1,len(node["children"])+1)])
        # metaInd must be decreased by 1 in order to compensate "1 refers to the first child node, 2 to the second, 3 to the third and so on" rule
 
def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample', inputData[:10])

    pos = 2
    stack = []
    stack.append([inputData[0], inputData[1], 0])

    nodeCounter = 0
    nodes = []
    nodes.append({"label":"N_0", "children":[]})


    while len(stack)>0 and pos<len(inputData):
        if stack[-1][0]==0:
            # log(len(stack)-1,"metadata", inputData[pos:pos+stack[-1][1]])
            nodes[stack[-1][2]]["metadata"] = inputData[pos:pos+stack[-1][1]]
            pos+=stack[-1][1]
            stack.pop(-1)
        else:
            stack[-1][0]-=1

            nodeCounter+=1
            childLabel = 'N_%d' % nodeCounter
            nodes[stack[-1][2]]['children'].append(childLabel)
            nodes.append({"label":childLabel, "children":[]})

            stack.append([inputData[pos], inputData[pos+1], len(nodes)-1])
            # log(childLabel, inputData[pos], inputData[pos+1])
            
            pos+=2

    flatNodes = arrayUtils.organize(nodes, 'label')

    calculateNodeValue('N_0', flatNodes)

    # for nodeLabel in flatNodes:
    #     log(nodeLabel, flatNodes[nodeLabel])

    result=flatNodes['N_0']['value']
    return (result,EXPECTED_RESULT)

 

