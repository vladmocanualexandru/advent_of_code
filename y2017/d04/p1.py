import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 466

def getInputData(inputFile):
    raw = getTuples_text(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])
    
    result=0

    for phrase in inputData:
        while len(phrase)>0:
            word = phrase[0]
            phrase.remove(word)
            if word in phrase:
                result -=1
                break

    result += len(inputData)

    return (result,EXPECTED_RESULT)

 
