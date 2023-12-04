import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 8467762

def convertToNumbers(strArr):
    return [int(entry) for entry in strArr if entry.isnumeric()]
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' | ')
    
    processed=[(convertToNumbers(entry[0].split(' ')[2:]), convertToNumbers(entry[1].split(' '))) for entry in raw]

    return processed 

def solution(inputFile):
    result = 0

    cards = getInputData(inputFile)

    cardCounts = [1 for card in cards]

    # log(cardCounts)

    for cardNo in range(len(cards)):
        card = cards[cardNo]
        noOfWins = len([number for number in card[0] if number in card[1]])

        if noOfWins == 0:
            continue

        for nextCardNo in range(cardNo+1, cardNo+noOfWins+1, 1):
            cardCounts[nextCardNo]+=cardCounts[cardNo]
        # log(cardCounts)

    # log(cardCounts)

    result = sum(cardCounts)

    return (result, EXPECTED_RESULT)