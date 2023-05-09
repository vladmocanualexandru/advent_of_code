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

EXPECTED_RESULT = 260
 
def getInputData(inputFile):
    raw = [entry[1:] for entry in getTuples_text(inputFile, ": ", ", ")]

    auntsDf = pd.DataFrame([], columns=['children','cats','samoyeds','pomeranians','akitas','vizslas','goldfish','trees','cars','perfumes'])


    for entry in raw:
        newAunt = {}
        
        for i in range(0,len(entry)-1,2):
            newAunt[entry[i]] = int(entry[i+1])

        auntsDf.loc[len(auntsDf)] = newAunt

    return auntsDf

def calculateScore(e):
    score = 1 if e["children"] == 3 else 0
    score += 1 if e["cats"] > 7 else 0
    score += 1 if e["samoyeds"] == 2 else 0
    score += 1 if e["pomeranians"] < 3 else 0
    score += 1 if e["akitas"] == 0 else 0
    score += 1 if e["vizslas"] == 0 else 0
    score += 1 if e["goldfish"] < 5 else 0
    score += 1 if e["trees"] > 3 else 0
    score += 1 if e["cars"] == 2 else 0
    score += 1 if e["perfumes"] == 1 else 0
    return score

def solution(inputFile):
    auntsDf = getInputData(inputFile)

    auntsDf["score"] = auntsDf.apply(calculateScore, axis=1)
    auntsDf.sort_values(by="score", ascending=False, inplace=True)

    result = auntsDf.index[0]+1

    return (result, EXPECTED_RESULT)