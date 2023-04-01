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

EXPECTED_RESULT = 709
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, " would ", " happiness units by sitting next to ", ".")
    
    processed=pd.DataFrame([entry[:-1]  for entry in raw], columns=["personA", "happiness_dirty", "personB"])
    processed["happiness"] = processed["happiness_dirty"].apply(lambda e : int(e.replace("gain ", "").replace("lose ", "")) * (-1 if "lose" in e else 1))
    processed.drop("happiness_dirty", axis=1, inplace=True)


    return processed

def calculateHappiness(peopleArrangement, connections):
    result = 0
    n = len(peopleArrangement)

    for i in range(0,n):
        personLeft = peopleArrangement[(i-1)%n]
        personCenter = peopleArrangement[i]
        personRight = peopleArrangement[(i+1)%n]

        result += connections[(connections["personA"]==personCenter) & (connections["personB"]==personLeft)]["happiness"].values
        result += connections[(connections["personA"]==personCenter) & (connections["personB"]==personRight)]["happiness"].values

    return result[0]

def calculateBestArrangement(chosen, all, connections, solutions):
    personFound = False
    for person in all:
        if person not in chosen:
            calculateBestArrangement(chosen+[person], all, connections, solutions)
            personFound=True

    if not personFound:
        solutions.append((chosen, calculateHappiness(chosen, connections)))
        log(len(solutions))

def solution(inputFile):
    connections = getInputData(inputFile)
    connections["personA2"] = connections.apply(lambda e : e["personA"] if e["personA"]<e["personB"] else e["personB"], axis=1)
    connections["personB2"] = connections.apply(lambda e : e["personB"] if e["personA"]<e["personB"] else e["personA"], axis=1)
    connections = connections.drop(columns=["personA", "personB"], axis=1).sort_values(by=["personA2", "personB2"]).groupby(by=["personA2","personB2"]).sum().reset_index()
    connections = connections.sort_values(by="happiness", ascending=False).reset_index()

    connections["removed"] = True

    neighbourCount = {}

    for index, row in connections.copy().iterrows():
        if not row["personA2"] in neighbourCount:
            neighbourCount[row["personA2"]] = 0
        if not row["personB2"] in neighbourCount:
            neighbourCount[row["personB2"]] = 0

        if neighbourCount[row["personA2"]]<2 and neighbourCount[row["personB2"]]<2:
            connections.at[index, 'removed'] = False
            neighbourCount[row["personA2"]]+=1
            neighbourCount[row["personB2"]]+=1  

    result = np.sum(connections[connections["removed"]==False]["happiness"])         

    return (result,EXPECTED_RESULT)