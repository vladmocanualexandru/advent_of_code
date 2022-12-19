import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 4982961

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    return raw


def solution(inputFile):
    inputData = getInputData(inputFile)

    def calculateFuelFuel(fuel):
        fuelFuel = math.floor(fuel/3)-2
        
        if fuelFuel<=0:
            return 0
        else:
            return fuelFuel+calculateFuelFuel(fuelFuel)

    result = 0

    for moduleMass in inputData:
        reqFuel = math.floor(moduleMass/3)-2
        result += reqFuel

        fuelFuel = calculateFuelFuel(reqFuel)
        
        result += fuelFuel

    return (result,EXPECTED_RESULT)

 
