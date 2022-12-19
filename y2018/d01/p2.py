import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 83173

def getInputData(inputFile):
    raw = getStrings(inputFile)
    data = [(r[0], int(r[1:])) for r in raw]
    return data

def solution(inputFile):
    data = getInputData(inputFile)

    freq = 0
    freqSet = {freq}

    index = 0
    while(True):
        t = data[index]
        freq+=t[1] if t[0]=='+' else (-t[1])
        if freq in freqSet:
            return (freq,EXPECTED_RESULT)
        else:
            freqSet.add(freq)
            index=(index+1)%len(data)

 
