import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw

    return processed 

def solution(inputFile):

    inputRaw = getInputData(inputFile)

    brackets = {'(':')', '[':']', '{':'}', '<':'>'}
    bracketScore = {')':3, ']':57, '}':1197, '>':25137}

    expected = []

    result = 0
    for line in inputRaw:
        expected = []
        # log(line)

        for b in line:
            # log(expected)
            if b in brackets:
                expected.append(brackets[b])
            else:
                if expected[-1]==b:
                    expected.pop(-1)
                else:
                    # log(line, 'Syntax error!')
                    result += bracketScore[b]
                    break

        # if len(expected)>0:
            # log('Incomplete!')
    
    return (result,288291)