import sys, os, re

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 118

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def hasAbbaString(strings):
    for string in strings:
        for i in range(len(string)-3):
            if string[i:i+2] == string[i+3]+string[i+2] and string[i]!=string[i+1]:
                return True
    
    return False
        
def solution(inputFile):
    input = getInputData(inputFile)
    # input = [
    #     'abba[mnop]qrst',
    #     'abcd[bddb]xyyx',
    #     'aaaa[qwer]tyui',
    #     'ioxxoj[asdfgh]zxcvbn'
    # ]

    # cleanInput = []

    result = 0
    for ip in input:
        if not hasAbbaString(re.findall("\[(\w+)", ip)):
            if hasAbbaString([ip]):
                # log(ip)
                result+=1

    return (result,EXPECTED_RESULT)

 