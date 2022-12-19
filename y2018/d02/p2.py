from itertools import count
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 'tiwcdpbseqhxryfmegkvjujvza'

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    result = None
    for text1 in inputData:
        for text2 in inputData:
            if text1 == text2:
                continue
            
            diffs=0
            for i in range(len(text1)):
                if text1[i]!=text2[i]:
                    diffs+=1
                
                if diffs==2:
                    break
            
            if diffs==1:
                result = (text1, text2)
                return (result[0],EXPECTED_RESULT)

    return (result[0],EXPECTED_RESULT)

 
