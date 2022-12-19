import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))
sys.path.append(os.path.abspath(os.path.join('..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

import y2019.int_code_computer as int_code_computer
 
EXPECTED_RESULT = 3654868

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    processed[1]=12
    processed[2]=2

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    mem = int_code_computer.initializeMemory(inputData)
    int_code_computer.run(mem)

    result=inputData[0]

    return (result,EXPECTED_RESULT)

 
