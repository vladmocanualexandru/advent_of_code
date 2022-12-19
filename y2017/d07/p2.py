import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 193

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' (', ')', ' -> ', ', ')
    
    processed=[(r[0], int(r[1]), r[3:]) for r in raw]

    return processed 

def calculateWeight(program, programs):
    programs[program]['totalWeight'] = programs[program]['weight'] + sum([calculateWeight(p, programs) for p in programs[program]['programs']])
    return programs[program]['totalWeight']

def calculateCorrectWeight(children, programs):
    if len(children) == 0:
        return None

    weights = [programs[p]['totalWeight'] for p in children]
    weights.sort()

    if weights[0] != weights[-1]:
        oddWeight = weights[0] if weights[0]!=weights[1] else weights[-1]
        correctWeight = weights[0] if weights[0]==weights[1] else weights[-1]

        for childLabel in children:
            child = programs[childLabel]
            if child['totalWeight'] == oddWeight:
                result = child['weight'] - (oddWeight-correctWeight)
                
                childResult = calculateCorrectWeight(child['programs'], programs)
                if childResult != None:
                    result = childResult

        return result
    else:
        return None


MASTER_PROGRAM = 'cyrupz'
def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample', inputData[:10])

    programs = {}

    for entry in inputData:
        if not entry[0] in programs:
            programs[entry[0]] = {"weight":entry[1], "totalWeight":-1, "programs":[]}

        programs[entry[0]]["programs"] = entry[2]

    calculateWeight(MASTER_PROGRAM, programs)

    result=calculateCorrectWeight(programs[MASTER_PROGRAM]['programs'], programs)
    return (result,EXPECTED_RESULT)

 

