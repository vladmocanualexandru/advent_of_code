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

EXPECTED_RESULT = 518
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    replacements=[(entry[0],entry[2]) for entry in raw[:-2]]

    return (replacements, raw[-1][0])

def solution(inputFile):
    (replacements, molecule)    = getInputData(inputFile)
    # log(replacements)
    # log(molecule)

    newMolecules = []

    for replacement in replacements:
        targetLen = len(replacement[0])
        for charI in range(0,len(molecule)-targetLen+1, 1):
            if molecule[charI:charI+targetLen] == replacement[0]:
                newMolecule = molecule[:charI]+replacement[1]+molecule[charI+targetLen:]
                if not newMolecule in newMolecules:
                    newMolecules.append(newMolecule)

    # log(newMolecules)

    result = len(newMolecules)
    return (result, EXPECTED_RESULT)