import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 191164

def getInputData(inputFile):
    raw = getTuples_text(inputFile,',', ':')
    
    processed=[entry.replace('[',"").replace(']',"").replace('{',"").replace('}',"") for entry in raw[0]]

    return processed 

def solution(inputFile):
    items = getInputData(inputFile)

    result=0
    for item in items:
        try:
            result += int(item)
        except ValueError:
            continue

    return (result,EXPECTED_RESULT)