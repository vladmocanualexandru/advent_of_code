import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 4956

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed=raw[0]

    return processed 

def fullyReact(polymer, targetPairs):
    while True:
        currentLen = len(polymer)
        for targetPair in targetPairs:
            polymer = polymer.replace(targetPair[0], '').replace(targetPair[1], '')
        
        if len(polymer) == currentLen:
            break

    return polymer

def solution(inputFile):
    original = getInputData(inputFile)

    targetPairs = [ ('%s%s' % (c, c.upper()), '%s%s' % (c.upper(),c), ) for c in list(string.ascii_lowercase)]

    result=len(original)
    for targetPair in targetPairs:
        polymerCandidate = original.replace(targetPair[0][0], '').replace(targetPair[0][1], '')
        
        result = min(result, len(fullyReact(polymerCandidate, targetPairs)))
    
    return (result,EXPECTED_RESULT)

 
