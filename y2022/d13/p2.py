import sys, os, math, json
import numpy as np
import pandas as pd
from functools import cmp_to_key

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 24477

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=[json.loads(entry) for entry in raw if entry != '']

    return processed 

def compare(a,b):
    # handle different types
    if not type(a) is type(b):
        if  type(a) is list:
            return compare(a, [b])
        else:
            return compare([a], b)

    # handle both are ints
    if type(a) is int:
        return a-b
    
    # handle both are arrays
    for index in range(min(len(a),len(b))):
        result = compare(a[index],b[index])
        if result != 0:
            return result

    # handle identical arrays with different sizes
    return len(a)-len(b)

def solution(inputFile):
    packets = getInputData(inputFile)

    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(compare))

    result=0
    for packetIndex in range(len(packets)):
        if packets[packetIndex] == [[2]]:
            result = packetIndex+1
        elif packets[packetIndex] == [[6]]:
            result *= (packetIndex+1)
            break
    else:
        log(red("Missing dividers"))

    return (result,EXPECTED_RESULT)