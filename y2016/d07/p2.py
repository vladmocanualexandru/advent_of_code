import sys, os, re

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 260

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def extractAbbaStrings(strings):
    result = []
    for string in strings:
        for i in range(len(string)-2):
            if string[i] == string[i+2] and string[i]!=string[i+1]:
                result.append(string[i:i+3])
    
    return result
        
def solution(inputFile):
    input = getInputData(inputFile)
    # input = [
    #     'aba[bab]xyz',
    #     'xyx[xyx]xyx',
    #     'aaa[kek]eke'
    # ]

    # cleanInput = []

    reg =  "\[(\w+)"

    result = 0
    for ip in input:
        hypernetABBAs = extractAbbaStrings(re.findall(reg, ip))
        ip = re.sub(reg, '', ip)
        if len(hypernetABBAs)>0:
            for hABBA in hypernetABBAs:
                if (hABBA[1]+hABBA[0]+hABBA[1]) in ip:
                    # log(hABBA,ip)
                    result += 1
                    break

    return (result,EXPECTED_RESULT)

 