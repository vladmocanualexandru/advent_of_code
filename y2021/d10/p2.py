import sys, os, statistics

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
    bracketScore = {')':1, ']':2, '}':3, '>':4}

    expected = []

    results = []

    # incompleteLines = []
    for line in inputRaw:
        expected = []
        # log(line)

        nextLine=False
        for b in line:
            # log(expected)
            if b in brackets:
                expected.append(brackets[b])
            else:
                if expected[-1]==b:
                    expected.pop(-1)
                else:
                    # log(line, 'Syntax error!')
                    nextLine = True
                    break

        if not nextLine and len(expected)>0:
            # log('Incomplete!')
            # log(expected)
            result = 0

            for c in range(len(expected)-1, -1, -1):
                result*=5
                result += bracketScore[expected[c]]

            results.append(result)

    return (statistics.median(results),820045242)