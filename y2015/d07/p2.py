import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 14134

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' -> ')
    
    processed=raw

    return processed 

wires = {}

signalCache = {}

def getWireDefinition(wire):
    if wire in signalCache:
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

    return value

def solution(inputFile):
    inputData = getInputData(inputFile)

    for instruction in inputData:
        wires[instruction[1]]=instruction[0].split(' ')

    wires['b'] = ['46065']

    result = explain('a')

    return (result, EXPECTED_RESULT)

 