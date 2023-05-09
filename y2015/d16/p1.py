import sys, os, math
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 373
 
def getInputData(inputFile):
    raw = [entry[1:] for entry in getTuples_text(inputFile, ": ", ", ")]

    auntsDf = pd.DataFrame([[3,7,2,3,0,0,5,3,2,1]], columns=['children','cats','samoyeds','pomeranians','akitas','vizslas','goldfish','trees','cars','perfumes'])

    for entry in raw:
        newAunt = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}
        
        for i in range(0,len(entry)-1,2):
            newAunt[entry[i]] = int(entry[i+1])

        auntsDf.loc[len(auntsDf)] = newAunt

    return auntsDf

def solution(inputFile):
    auntsDf = getInputData(inputFile)

    # calculate similarity between values but keep only first entry of the response
    # that will indicate the similarity between all values and the first value aka the goal aunt
    similarity = pd.Series(cosine_similarity(auntsDf)[0]).sort_values(ascending=False)

    # sorting desc will place the goal aunt on position 0 and target aunt on position 1
    result = similarity.index[1]

    return (result, EXPECTED_RESULT)