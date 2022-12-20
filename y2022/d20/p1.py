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
    raw = getNumbers_dec(inputFile)
    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    numbers = getInputData(inputFile)

    for number in ([]+numbers):
        currentPos = numbers.index(number)
        numbers.remove(number)

        newPos = (currentPos+number)%len(numbers)
        numbers = numbers[:newPos]+[number]+numbers[newPos:]

    index0 = numbers.index(0)

    result = numbers[(index0+1000)%len(numbers)]
    result += numbers[(index0+2000)%len(numbers)]
    result += numbers[(index0+3000)%len(numbers)]

    return result