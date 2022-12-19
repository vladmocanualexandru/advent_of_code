import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 46065

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' -> ')
    
    processed=raw

    return processed 

wires = {}

signalCache = {}

def getWireDefinition(wire):
    if wire in signalCache:
        # log('Found cached value: %s=%s' % (wire, signalCache[wire]))
        return signalCache[wire]
    else:
        return explain(wire)

def explain(wire):
    if not wire in wires:
        return int(wire)

    wireDef = wires[wire]

    value = -1
    if len(wireDef)==1:
        value = getWireDefinition(wireDef[0])

    elif len(wireDef)==2:
        value = 65536+(~getWireDefinition(wireDef[1]))
    else:
        operator = wireDef[1]

        if operator == 'AND':
            value =  getWireDefinition(wireDef[0])&getWireDefinition(wireDef[2])
        elif operator == 'OR':
            value =  getWireDefinition(wireDef[0])|getWireDefinition(wireDef[2])
        elif operator == 'LSHIFT':
            value =  getWireDefinition(wireDef[0])<<getWireDefinition(wireDef[2])
        else:
            value =  getWireDefinition(wireDef[0])>>getWireDefinition(wireDef[2])
    
    if wire not in signalCache:
        signalCache[wire] = value
        # log('Saved cached value: %s=%s' % (wire, value))

    return value

def solution(inputFile):
    inputData = getInputData(inputFile)

    # input = [
    #     ['123','f'],
    #     ['NOT h','b'],
    #     ['789','h'],
    #     ['f LS 1','d'],
    #     ['b AND c','a'],
    #     ['g RS 2','e'],
    #     ['d OR e','c'],
    #     ['456','g'],
    # ]

    for instruction in inputData:
        wires[instruction[1]]=instruction[0].split(' ')

    result = explain('a')
    
    return (result, EXPECTED_RESULT)

 