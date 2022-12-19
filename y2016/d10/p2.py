import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 22847

def getInputData(inputFile):
    raw = getStrings(inputFile)

    botRules = []
    valueRules = []
    
    for rule in raw:
        if 'gives low to ' in rule:
            botRules.append(rule)
        else:
            valueRules.append(rule)

    processed = {"botRules":botRules,"valueRules":valueRules}

    return processed 


def solution(inputFile):
    rules = getInputData(inputFile)
    # log(rules)

    bots = {}
    outputs = {}

    for botRule in rules["botRules"]:
        tkns = botRule.split(" gives low to ")
        tkns2 = tkns[1].split(' and high to ')

        minReceiver = tkns2[0]
        maxReceiver = tkns2[1]
        bots[tkns[0]] = {"logic":{"min":minReceiver, "max":maxReceiver}, "values" : []}

        if 'output' in minReceiver:
            outputs[minReceiver] = []
      
        if 'output' in maxReceiver:
            outputs[maxReceiver] = []
      
    for valueRule in rules["valueRules"]:
        tkns = valueRule.split(" goes to ")
      
        bots[tkns[1]]["values"].append(int(tkns[0][6:]))

    allMovesDone = False
    while not allMovesDone:
        allMovesDone = True

        for botName in bots:
            bot = bots[botName]

            if len(bot["values"]) == 2:
                allMovesDone = False
                minReceiver = bot["logic"]["min"]
                minValue = min(bot["values"])
                maxReceiver = bot["logic"]["max"]
                maxValue = max(bot["values"])

                if 'output' in minReceiver:
                    outputs[minReceiver].append(minValue)
                else:
                    bots[minReceiver]["values"].append(minValue)

                if 'output' in maxReceiver:
                    outputs[maxReceiver].append(maxValue)
                else:
                    bots[maxReceiver]["values"].append(maxValue)

                bot["values"].clear()

    result = outputs['output 0'][0]
    result *= outputs['output 1'][0] 
    result *= outputs['output 2'][0] 

    return (result,EXPECTED_RESULT)

 

