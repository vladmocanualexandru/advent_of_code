import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 'usccerug'

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):
    input = getInputData(inputFile)
    # input = [
    # 'eedadn',
    # 'drvtee',
    # 'eandsr',
    # 'raavrd',
    # 'atevrs',
    # 'tsrnev',
    # 'sdttsa',
    # 'rasrtv',
    # 'nssdts',
    # 'ntnada',
    # 'svetve',
    # 'tesnvt',
    # 'vntsnd',
    # 'vrdear',
    # 'dvrsen',
    # 'enarar'
    # ]

    letters = string.ascii_lowercase


    result = ''

    for i in range(len(input[0])):
        counts = [0 for a in range(len(letters))]
        for j in range(len(input)):
            counts[letters.index(input[j][i])]+=1
        
        result = result+letters[counts.index(max(counts))]

    return (result,EXPECTED_RESULT)

 