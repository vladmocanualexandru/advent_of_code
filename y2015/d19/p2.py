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

EXPECTED_RESULT = 200

END_MOLECULE = 'e'
MAX_STEPS = pow(10,10)
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    replacements=[(entry[2],entry[0]) for entry in raw[:-2]]

    return (replacements, raw[-1][0])

# def performReplacement(currentMolecule, targetMolecule, replacements, currentSteps, minSteps):
#     if len(currentMolecule) ==0 or currentSteps>=minSteps:
#         return minSteps

#     if currentMolecule == targetMolecule:
#         log(currentSteps)
#         return currentSteps
    
#     innerMinSteps = minSteps
#     for replacement in replacements:
#         markerLen = len(replacement[0])

#         for charI in range(0, len(currentMolecule)-markerLen+1, 1):
#             if currentMolecule[charI:charI+markerLen] == replacement[0]:
#                 newMolecule = currentMolecule[:charI]+replacement[1]+currentMolecule[charI+markerLen:]
#                 innerMinSteps = min(innerMinSteps, performReplacement(newMolecule, targetMolecule, replacements, currentSteps+1, innerMinSteps))

#     return innerMinSteps

# GREEDY SOLUTION - somehow it works - might not work for all cases - worked for mine #yay Thanks to  my lovely wife for coming up with the idea of reversing the logic!
def solution(inputFile):
    (replacements, startMolecule) = getInputData(inputFile)

    result = 0

    while startMolecule  != END_MOLECULE:
        for replacement in replacements:
            if replacement[0] in startMolecule:
                # log(startMolecule)
                startMolecule = startMolecule.replace(replacement[0], replacement[1], 1)
                result+=1
                break

    # result = performReplacement(startMolecule, END_MOLECULE, replacements, 0, MAX_STEPS)

    return (result, EXPECTED_RESULT)