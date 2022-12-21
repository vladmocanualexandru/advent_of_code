import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, ": ")
    
    phase1=[[entry[0], entry[1].split(' ')] for entry in raw]
    phase2=[[entry[0], entry[1] if len(entry[1])>1 else int(entry[1][0])] for entry in phase1]

    return phase2

def calculate(a, op, b):
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == '/':
        return a/b
    if op == '*':
        return a*b

def getValue(name, monkeys):
    monkey = monkeys[name]

    if monkey["value"] != None:
        return monkey["value"]
    else:
        valueDef = monkey["valueDef"]
        return calculate(getValue(valueDef[0], monkeys),valueDef[1],getValue(valueDef[2], monkeys))


def solution(inputFile):
    monkeyData = getInputData(inputFile)

    monkeys = {}

    for [name,data] in monkeyData:
        newMonkey = {"value":None, "valueDef":None}

        if type(data) is int:
            newMonkey["value"] = data
        else:
            newMonkey["valueDef"] = data

        monkeys[name] = newMonkey

    return int(getValue("root", monkeys))