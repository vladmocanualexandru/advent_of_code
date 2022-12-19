import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 53

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def isNiceString(string):
    hasPairWithLetterBetween = False
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            hasPairWithLetterBetween = True
            break

    foundPair = False
    for i in range(len(string)-3):
        for j in range(i+2, len(string)-1):
            if string[i]+string[i+1] == string[j]+string[j+1]:
                foundPair = True
                break

        if foundPair:
            break

    return hasPairWithLetterBetween and foundPair


def solution(inputFile):
    inputData = getInputData(inputFile)

    result =  0
    for string in inputData:
        # log(string, isNiceString(string))
        if isNiceString(string):
            result += 1

    return (result, EXPECTED_RESULT)

 