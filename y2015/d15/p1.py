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

EXPECTED_RESULT = 222870
 
def getInputData(inputFile):
    rawDf = pd.DataFrame(getTuples_text(inputFile, ": capacity ",", durability ", ", flavor ", ", texture ",", calories "),
                      columns=["ingredient", "capacity", "durability", "flavor", "texture", "calories"]).set_index("ingredient")

    rawDf["capacity"] = pd.to_numeric(rawDf["capacity"])
    rawDf["durability"] = pd.to_numeric(rawDf["durability"])
    rawDf["flavor"] = pd.to_numeric(rawDf["flavor"])
    rawDf["texture"] = pd.to_numeric(rawDf["texture"])
    rawDf["calories"] = pd.to_numeric(rawDf["calories"])

    return rawDf 

def solution(inputFile):
    ingredients = getInputData(inputFile)
    
    candidates = [[t1,t2,t3,100-t1-t2-t3] for t1 in range(1,98,1) for t2 in range(1, 99-t1, 1) for t3 in range(1, 100-t1-t2)]

    for prop in ["capacity", "durability", "flavor", "texture"]:
        filteredCandidates = []
        for candidate in candidates:
            value = candidate[0]*ingredients.iloc[0][prop]
            value += candidate[1]*ingredients.iloc[1][prop]
            value += candidate[2]*ingredients.iloc[2][prop]
            value += candidate[3]*ingredients.iloc[3][prop]

            if value > 0:
                filteredCandidates.append(candidate+[value])

        candidates = filteredCandidates

    candidatesDf = pd.DataFrame(candidates)

    candidatesDf["prod"] = candidatesDf[4] * candidatesDf[5] * candidatesDf[6] * candidatesDf[7]

    result = np.max(candidatesDf["prod"])
        
    return (result, EXPECTED_RESULT)