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

EXPECTED_RESULT = None
 
def getInputData(inputFile):
    rawDf = pd.DataFrame(getTuples_text("y2015/d15/input.txt", ": capacity ",", durability ", ", flavor ", ", texture ",", calories "),
                      columns=["ingredient", "capacity", "durability", "flavor", "texture", "calories"]).set_index("ingredient")

    rawDf["capacity"] = pd.to_numeric(rawDf["capacity"])
    rawDf["durability"] = pd.to_numeric(rawDf["durability"])
    rawDf["flavor"] = pd.to_numeric(rawDf["flavor"])
    rawDf["texture"] = pd.to_numeric(rawDf["texture"])
    rawDf["calories"] = pd.to_numeric(rawDf["calories"])

    return rawDf 

def solution(inputFile):
    ingredients = getInputData(inputFile)
    
    log(ingredients)

    candidates = [(t1,t2,t3,100-t1-t2-t3) for t1 in range(1,98,1) for t2 in range(1, 99-t1, 1) for t3 in range(1, 100-t1-t2)]

    log(len(candidates))

    result = 0
    for candidate in candidates:
        (t1,t2,t3,t4) = candidate

        


    result = 0
    # for t1 in range(1,98,1):
        
    #     for t2 in range(1,99-t1,1):
    #         for t3 in range(1,100-t1-t2,1):
    #             t4 = 100-t1-t2-t3

    #             # log(t1,t2,t3,t4)
    #             # recipe = ingredients.copy()

    #             # recipe.iloc[0] = recipe.iloc[0] * t1
    #             # recipe.iloc[1] = recipe.iloc[1] * t2 
    #             # recipe.iloc[2] = recipe.iloc[2] * t3
    #             # recipe.iloc[3] = recipe.iloc[3] * t4

    #             # capacity = np.sum(recipe["capacity"])
    #             # durability = np.sum(recipe["durability"])
    #             # flavor = np.sum(recipe["flavor"])
    #             # texture = np.sum(recipe["texture"])

    #             # if np.min([capacity,durability,flavor,texture])>0:
    #             #     result = max(result, capacity*durability*flavor*texture)
    #             #     log(result)
        
    return (result, EXPECTED_RESULT)