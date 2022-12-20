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

from functools import cmp_to_key

import y2022.d18.surfaceCounter as surfaceCounter
 
def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, ',')
    
    processed=[(entry[0],entry[1],entry[2]) for entry in raw]

    return processed 

def solution(inputFile):
    cubes = getInputData(inputFile)

    return surfaceCounter.countSurfaces(cubes)