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

from y2022.d20.decryptor import decrypt

MIX_COUNT = 1
DECRYPTION_KEY = 1

REF_VALUE=0
GPS_INDEX_0=1000
GPS_INDEX_1=2000
GPS_INDEX_2=3000

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=[(raw[entryIndex],entryIndex) for entryIndex in range(len(raw))]

    return processed 

def solution(inputFile):
    numbers = getInputData(inputFile)
    return decrypt(numbers, DECRYPTION_KEY,MIX_COUNT,REF_VALUE,GPS_INDEX_0,GPS_INDEX_1,GPS_INDEX_2)