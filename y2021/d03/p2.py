import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getBitRatio(data, digit_i):
    ratio = 0

    for input_i in range(len(data)):
        digit = int(data[input_i][digit_i])
        
        ratio += pow(-1, digit+1)
    
    return  ratio

def filterData(data, mostCommon=True):

    input_len = len(data)
    
    for digit_i in range(input_len):
        if len(data)==1:
            break

        ratio = getBitRatio(data, digit_i)

        if mostCommon == False:
            ratio*=-1

        pop_i = 0
        while len(data)>1 and pop_i<len(data):
            digit = int(data[pop_i][digit_i])

            should_pop = digit == 1 and ratio<0
            should_pop = should_pop or (digit == 0 and ratio>0)

            if mostCommon == True:
                should_pop = should_pop or (ratio==0 and digit == 0)
            else:
                should_pop = should_pop or (ratio==0 and digit == 1)

            if should_pop:
                data.pop(pop_i)
                pop_i-=1
            
            pop_i+=1

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=[r for r in raw]

    return processed 

def solution(inputFile):

    # input =  ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    input = getInputData(inputFile)

    o2_input = [] + input
    scrub_input = [] + input

    filterData(o2_input)
    filterData(scrub_input, False)

    o2_rate = int(o2_input[0],2)
    scrub_rate = int(scrub_input[0],2)

    life = o2_rate*scrub_rate

    # log("o2_rate: ",  o2_rate)
    # log("scrub_rate: ",  scrub_rate)
    # log("RESULT: ",  life)

    return (life, 4672151)