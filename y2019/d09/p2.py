import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))
sys.path.append(os.path.abspath(os.path.join('..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

import y2019.int_code_computer as int_code_computer
 
EXPECTED_RESULT = 70634

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    return processed 


def solution(inputFile):
    instructions = getInputData(inputFile)
    # log('input sample', instructions[:10])

    mem = int_code_computer.initializeMemory(instructions)
    mem['input'] = [2]
    result=int_code_computer.run(mem, 0)[1][0]
    return (result,EXPECTED_RESULT)

 

