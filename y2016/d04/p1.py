import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 173787

def parseRoom(room):
    tkns = room[-1].split('[')
    return [''.join(room[:-1]), int(tkns[0]), tkns[1][:-1]]

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'-')
    
    processed=[parseRoom(room) for room in raw]

    return processed 


def countChars(string):
    counts = {}
    for c in string:
        if not c in counts:
            counts[c] = 1
        else:
            counts[c] +=1
    
    return counts

def computeChecksum(counts):
    countTuples = [(i, counts[i]) for i in counts]
    countTuples.sort(key = lambda x: (-x[1], x[0]))

    return ''.join(t[0] for t in countTuples)[:5]


def solution(inputFile):
    input = getInputData(inputFile)

    result = 0
    for room in input:
        checksum = computeChecksum(countChars(room[0]))
        if checksum==room[2]:
            result+=room[1]

    return (result,EXPECTED_RESULT)

 