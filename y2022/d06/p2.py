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
 
EXPECTED_RESULT = 2313

def getInputData(inputFile):
    raw = getStrings(inputFile)[0]
    
    processed=raw

    return processed 

def solution(inputFile):
    signal = getInputData(inputFile)

    result=None
    for charIndex in range(0, len(signal)-4):
        message = list(signal[charIndex:charIndex+14])
        message.sort()

        messageFound = True
        for checkIndex in range(0, 13):
            if message[checkIndex]==message[checkIndex+1]:
                messageFound = False
                break

        if messageFound:
            result = charIndex+14
            break

    return (result,EXPECTED_RESULT)