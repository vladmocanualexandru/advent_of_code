import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 'BGJCNLQUYIFMOEZTADKSPVXRHW'

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' must be finished before step ','Step ',' can begin.')
    
    processed=[(r[1], r[2]) for r in raw]

    componentsConfig = {}
    for entry in processed:
        if not entry[0] in componentsConfig:
            componentsConfig[entry[0]] = {"requirements":[]}
        if not entry[1] in componentsConfig:
            componentsConfig[entry[1]] = {"requirements":[]}

        componentsConfig[entry[1]]["requirements"].append(entry[0])

    components = [(config, componentsConfig[config]["requirements"]) for config in componentsConfig]
    components.sort(key=lambda e:e[0])

    return components 


def solution(inputFile):
    components = getInputData(inputFile)
    # log(components)

    result=[]
    while len(components)>0:
        for component in []+components:
            if len(component[1])==0:
                result.append(component[0])
                for component2 in components:
                    if component[0] in component2[1]:
                        component2[1].remove(component[0])
                components.remove(component)
                break



    return (''.join(result),EXPECTED_RESULT)

 

