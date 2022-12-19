import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *


def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=[r for r in raw]

    return processed 


def solution(inputFile):

    input = getInputData(inputFile)
    
    result = 0

    for index in range(len(input)-1):
        if input[index+1]>input[index]:
            result = result + 1

    return (result,1215)