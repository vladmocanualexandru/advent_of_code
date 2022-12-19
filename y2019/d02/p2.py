import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))
sys.path.append(os.path.abspath(os.path.join('..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

import y2019.int_code_computer as int_code_computer
 
EXPECTED_RESULT = 7014

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    target = 19690720

    for noun in range(100):
        for verb in range(100):

            dataCopy = [] + inputData
            dataCopy[1] = noun
            dataCopy[2] = verb

            mem = int_code_computer.initializeMemory(dataCopy)
            int_code_computer.run(mem)

            if dataCopy[0] == target:
                return (100*noun+verb,EXPECTED_RESULT)

    return (None,EXPECTED_RESULT)

 
