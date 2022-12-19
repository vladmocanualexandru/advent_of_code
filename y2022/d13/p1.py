import sys, os, math, json
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 5825

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

    result=0
    for packetIndex in range(0, len(packets), 2):
        p0 = packets[packetIndex]
        p1 = packets[packetIndex+1]

        outcome = compare(p0, p1)

        if outcome<0:
            result+=packetIndex/2+1


    return (int(result),EXPECTED_RESULT)