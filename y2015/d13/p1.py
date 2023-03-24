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
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, " would ", " happiness units by sitting next to ", ".")
    
    processed=pd.DataFrame([entry[:-1]  for entry in raw], columns=["nodeA", "weight_dirty", "nodeB"])
    processed["weight"] = processed["weight_dirty"].apply(lambda e : int(e.replace("gain ", "").replace("lose ", "")) * (-1 if "lose" in e else 1))
    processed.drop("weight_dirty", axis=1, inplace=True)


    return processed

def calculateHappiness(peopleArrangement, connections):
    result = 0
    n = len(peopleArrangement)

    for i in range(0,n):
        personLeft = peopleArrangement[(i-1)%n]
        personCenter = peopleArrangement[i]
        personRight = peopleArrangement[(i+1)%n]

        result += connections[(connections["nodeA"]==personCenter) & (connections["nodeB"]==personLeft)]["weight"].values
        result += connections[(connections["nodeA"]==personCenter) & (connections["nodeB"]==personRight)]["weight"].values

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

    people = connections["nodeA"].unique()

    solutions = []
    calculateBestArrangement([], people, connections, solutions)

    solutions = pd.DataFrame(solutions, columns = ["people", "happiness"]).sort_values(by="happiness", ascending=False)

    return solutions.head(1)