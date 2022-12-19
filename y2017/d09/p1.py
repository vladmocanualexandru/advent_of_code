import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 7640

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw[0].replace('!!','')

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input sample (first 20)', inputData[:20])

    result = 0
    currentValue = 0
    garbageMode = False
    for index in range(len(inputData)):
        if not (index>0 and inputData[index-1]=='!'):
            c = inputData[index]
            if c == '<':
                garbageMode = True
            if c == '>':
                garbageMode = False
            elif not garbageMode and c == '{':
                currentValue+=1
            elif not garbageMode and c == '}':
                result+=currentValue
                currentValue-=1

    return (result,EXPECTED_RESULT)

 
