import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 258

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def isNiceString(string):
    vowels = ['a','e','i','o','u']
    disallowedStrings = ['ab', 'cd', 'pq', 'xy']
    vowelCount = 0
    doubleLetterFound = False

    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            doubleLetterFound = True
        
        if string[i] in vowels:
            vowelCount+=1

        if string[i]+string[i+1] in disallowedStrings:
            return False

    if string[-1] in vowels:
        vowelCount+=1

    return vowelCount>=3 and  doubleLetterFound

def solution(inputFile):
    inputData = getInputData(inputFile)

    result =  0
    for string in inputData:
        if isNiceString(string):
            result += 1

    return (result, EXPECTED_RESULT)

 