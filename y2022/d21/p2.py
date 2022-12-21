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

HUMAN_MONKEY_NAME = 'humn'
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, ": ")
    
    phase1=[[entry[0], entry[1].split(' ')] for entry in raw]
    phase2=[[entry[0], entry[1] if len(entry[1])>1 else int(entry[1][0])] for entry in phase1]

    return phase2

REVERSED_OPERATIONS={
    "+":"-",
    "-":"+",
    "*":"/",
    "/":"*"
}

def calculate(a, op, b, reversed=False):

    if reversed:
        op = REVERSED_OPERATIONS[op]

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

def getHumanValue(name, value, monkeys):
    [nameA, op, nameB] = monkeys[name]["valueDef"]

    if nameA == HUMAN_MONKEY_NAME or monkeys[nameA]["value"] == None:
        value = calculate(value, op, monkeys[nameB]["value"], reversed=True)

        if nameA == HUMAN_MONKEY_NAME:
            return value
        else:
            return getHumanValue(nameA, value, monkeys)
    elif nameB == HUMAN_MONKEY_NAME or monkeys[nameB]["value"] == None:
        if op=='+':
            value = calculate(value, "-", monkeys[nameA]["value"])
        elif op=='-':
            value = calculate(monkeys[nameA]["value"], "-", value)
        elif op=='*':
            value = calculate(value, "/", monkeys[nameA]["value"])
        elif op=='/':
            value = calculate(monkeys[nameA]["value"], "/", value)

        if nameB == HUMAN_MONKEY_NAME:
            return value
        else:
            return getHumanValue(nameB, value, monkeys)

def solution(inputFile):
    monkeyData = getInputData(inputFile)

    monkeys = {}

    for [name,data] in monkeyData:
        if name == HUMAN_MONKEY_NAME:
            continue
        
        newMonkey = {"value":None, "valueDef":None}

        if type(data) is int:
            newMonkey["value"] = data
        else:
            newMonkey["valueDef"] = data

        monkeys[name] = newMonkey

    monkeySimplified = True
    while monkeySimplified:
        monkeySimplified = False

        for name in monkeys:
            monkey = monkeys[name]
            if monkey["value"] == None:
                leftMonkeyName = monkey["valueDef"][0]
                rightMonkeyName = monkey["valueDef"][2]

                if leftMonkeyName == HUMAN_MONKEY_NAME or rightMonkeyName == HUMAN_MONKEY_NAME:
                    continue

                leftMonkey = monkeys[leftMonkeyName]
                rightMonkey = monkeys[rightMonkeyName]

                if leftMonkey["value"] != None and rightMonkey["value"] != None:
                    monkey["value"] = calculate(leftMonkey["value"], monkey["valueDef"][1],rightMonkey["value"])
                    monkeySimplified = True

    rootMonkey = monkeys["root"]

    result = None

    if monkeys[rootMonkey["valueDef"][0]]["value"] != None:
        result = getHumanValue(rootMonkey["valueDef"][2], monkeys[rootMonkey["valueDef"][0]]["value"], monkeys)
    else:
        result = getHumanValue(rootMonkey["valueDef"][0], monkeys[rootMonkey["valueDef"][2]]["value"], monkeys)

    return result