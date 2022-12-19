import sys, os, math
import numpy as np
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 8139


def getInputData(inputFile):
    priorities = {}
    for c in ascii_lowercase:
        priorities[c] = ord(c)-96
    for c in ascii_uppercase:
        priorities[c] = ord(c)-38


    raw = getStrings(inputFile)
    
    processed1=[(r[0:int(len(r)/2)],r[int(len(r)/2):]) for r in raw]
    processed2 = [([priorities[l1] for l1 in entry[0]], [priorities[l2] for l2 in entry[1]]) for entry in processed1]

    return processed2

def solution(inputFile):
    inputData = getInputData(inputFile)

    result=0
    for rucksack in inputData:
        pd1 = pd.DataFrame(rucksack[0], columns=["items"])
        pd2 = pd.DataFrame(rucksack[1], columns=["items"])

        result+=pd.merge(pd1, pd2, how="inner", on="items").iloc[0][0]

    return (result,EXPECTED_RESULT)