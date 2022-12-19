import sys, os, math, json
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 87842

def getInputData(inputFile):
    raw = getText(inputFile)
    
    processed={"data":json.loads(raw)}

    return processed 

def calculateValue(jsonData):
    if type(jsonData) is int:
        return jsonData
    if type(jsonData) is str:
        return 0

    result = 0
    
    if type(jsonData) is dict:
        for prop in jsonData:
            if jsonData[prop] == 'red':
                return 0
            else:
                result += calculateValue(jsonData[prop])
    elif type(jsonData) is list:
        for entry in jsonData:
            result += calculateValue(entry)
    
    return result

def solution(inputFile):
    jsonData = getInputData(inputFile)
    
    result = calculateValue(jsonData)

    return (result,EXPECTED_RESULT)