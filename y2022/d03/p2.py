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
 
EXPECTED_RESULT = 2668

def getInputData(inputFile):
    priorities = {}
    for c in ascii_lowercase:
        priorities[c] = ord(c)-96
    for c in ascii_uppercase:
        priorities[c] = ord(c)-38


    raw = getStrings(inputFile)
    
    processed2 = [[priorities[l] for l in entry] for entry in raw]

    return processed2

def solution(inputFile):
    rucksacks = getInputData(inputFile)

    result=0

    for i in range(0,len(rucksacks),3):
        pd1 = pd.DataFrame(rucksacks[i], columns=["items"])
        pd2 = pd.DataFrame(rucksacks[i+1], columns=["items"])
        pd3 = pd.DataFrame(rucksacks[i+2], columns=["items"])

        result += pd.merge(pd.merge(pd1, pd2, how="inner", on="items"), pd3, how="inner", on="items").iloc[0][0]

    return (result,EXPECTED_RESULT)