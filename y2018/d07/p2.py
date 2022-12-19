from random import random
import sys, os, time

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 1017

WORKER_COUNT = 5
STEP_DELAY = 60
SECOND_LENGTH = 0

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' must be finished before step ','Step ',' can begin.')
    
    processed=[(r[1], r[2]) for r in raw]

    componentsConfig = {}
    for entry in processed:
        if not entry[0] in componentsConfig:
            componentsConfig[entry[0]] = {"requirements":[], "timeToComplete": STEP_DELAY+ord(entry[0])-64}
        if not entry[1] in componentsConfig:
            componentsConfig[entry[1]] = {"requirements":[], "timeToComplete": STEP_DELAY+ord(entry[1])-64}

        componentsConfig[entry[1]]["requirements"].append(entry[0])

    components = [(config, componentsConfig[config]["requirements"], componentsConfig[config]["timeToComplete"]) for config in componentsConfig]
    components.sort(key=lambda e:e[0])

    return components 


def solution(inputFile):
    components = getInputData(inputFile)
    # log(components)

    workersStacks = [{"workingOn":'waiting', "remainingTime":-1} for i in range(WORKER_COUNT)]

    result = 0
    finished = []
    componentCount = len(components)
    while len(finished)<componentCount:
        for stack in workersStacks:
            if stack["remainingTime"]>0:
                stack["remainingTime"]-=1
            
            if stack["remainingTime"]==0:
                finished.append(stack["workingOn"])
                for component in components:
                    if stack["workingOn"] in component[1]:
                        component[1].remove(stack["workingOn"])

                stack["remainingTime"] = -1

        for component in []+components:
            if component[1] == []:
                for worker in workersStacks:
                    if worker["remainingTime"] == -1:
                        worker["workingOn"] = component[0]
                        worker["remainingTime"] = component[2]

                        components.remove(component)
                        break
        
        # log(result, '   '.join([stack["workingOn"] if stack["remainingTime"]>0 else '.' for stack in workersStacks]), ''.join(finished))
        time.sleep(SECOND_LENGTH)
        result+=1

    # the check for all components is done, after the second counter has been increased; the result is 1s lower than the counter
    return (result-1,EXPECTED_RESULT)

 

