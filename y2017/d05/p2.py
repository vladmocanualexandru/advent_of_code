from multiprocessing.dummy import current_process
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 28707598

def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    currentPosition = 0

    result=0
    while currentPosition<len(inputData) and currentPosition>-1:
        steps = inputData[currentPosition]
        
        if steps >= 3:
            inputData[currentPosition]-=1
        else:
            inputData[currentPosition]+=1

        result+=1
        currentPosition+=steps

    return (result,EXPECTED_RESULT)

 
