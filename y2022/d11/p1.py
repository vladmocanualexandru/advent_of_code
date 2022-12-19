import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 62491
ROUND_COUNT = 20

def createNewmonkey():
    return {
        "items":[],
        "operation": lambda e: pow(e,2),
        "opParam":-1,
        "test": [-1,-1,-1],
        "inspectionCount": 0
    }

def multiply(a,monkey):
    return a*monkey["opParam"]

def add(a,monkey):
    return a+monkey["opParam"]

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')

    processed = [createNewmonkey()]
    
    for t in raw:
        if t == ['']:
            processed.append(createNewmonkey())
            continue
        
        currentmonkey = processed[-1]
        if t[0] == 'Starting':
            currentmonkey["items"] = [int(n.replace(',','')) for n in t[2:]]
        elif t[0] == 'Operation:':
            op=None
            if t[5] == 'old':
                op = lambda e1,e2 : 2*e1
                if t[4] == '*':
                    op = lambda e1,e2 : pow(e1,2)
            else:
                currentmonkey["opParam"] = int(t[5])
                op = add
                if t[4] == '*':
                    op = multiply

            currentmonkey["operation"] = op

        elif t[0] == 'Test:':
            currentmonkey["test"][0] = int(t[-1])
        elif t[1] == 'true:':
            currentmonkey["test"][1] = int(t[-1])
        elif t[1] == 'false:':
            currentmonkey["test"][2] = int(t[-1])

    return processed 

def solution(inputFile):
    monkeys = getInputData(inputFile)

    for roundIndex in range(ROUND_COUNT):
        for monkey in monkeys:

            monkey["inspectionCount"] += len(monkey["items"])

            for item in monkey["items"]:
                item = int(monkey["operation"](item, monkey)/3)
                if item % monkey["test"][0] == 0:
                    monkeys[monkey["test"][1]]["items"].append(item)
                else:
                    monkeys[monkey["test"][2]]["items"].append(item)

            monkey["items"] = []

    inspectionCounts = pd.Series([monkey["inspectionCount"] for monkey in monkeys]).sort_values(ascending=False)
   
    result = inspectionCounts.iloc[0] * inspectionCounts.iloc[1]

    return (result,EXPECTED_RESULT)