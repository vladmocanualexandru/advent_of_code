import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[r for r in raw]

    return processed 

def solution(inputFile):

    # input =  ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    input = getInputData(inputFile)

    gamma_rate = 0
    epsilon_rate = 0

    input_len = len(input[0])

    for digit_i in range(input_len):
        ratio = 0

        for input_i in range(len(input)):
            digit = int(input[input_i][digit_i])
            
            ratio += pow(-1, digit+1)
        
        value = pow(2, input_len-digit_i-1)
        if ratio<0:
            gamma_rate+=value
        else:
            epsilon_rate+=value

    power = gamma_rate*epsilon_rate

    # log("gamma_rate: ",  gamma_rate)
    # log("epsilon_rate: ",  epsilon_rate)
    # log("RESULT: ",  power)

    return (power, 1092896)