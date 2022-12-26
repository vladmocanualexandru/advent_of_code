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
    raw = getStrings(inputFile)
    
    processed=[entry[::-1] for entry in raw]

    return processed 

def convertToDecimal(reversedSnafuNumber):
    result = 0

    for charIndex in range(len(reversedSnafuNumber)):
        digitChar = reversedSnafuNumber[charIndex]
        digit = -2
        if digitChar == '-':
            digit = -1
        elif digitChar in ["0","1","2"]:
            digit = int(digitChar)

        result += digit*pow(5,charIndex)

    return result

def convertToSnafu(decimalNumber):
    result = []

    while decimalNumber>0:

        result.append(decimalNumber%5)
        decimalNumber = math.floor(decimalNumber/5)

    finalResult = ""
    for digitIndex in range(len(result)-1):
        digit = result[digitIndex]
        if digit<=2:
            finalResult+="%d"%digit
        elif digit == 3:
            finalResult+="="
            result[digitIndex+1]+=1
        else:
            #  digit == 4
            finalResult+="-"
            result[digitIndex+1]+=1

    if result[-1] == 3:
            finalResult+="="
            finalResult+="1"
    elif result[-1] == 4:
            #  digit == 4
            finalResult+="-"
            finalResult+="1"
    else:
        finalResult+="%d"%result[-1]

    return finalResult[::-1]

def solution(inputFile):
    reversedSnafuNumbers = getInputData(inputFile)

    decimalSum = sum([convertToDecimal(reversedSnafuNumber) for reversedSnafuNumber in reversedSnafuNumbers])

    return convertToSnafu(decimalSum)