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

EXPECTED_RESULT = 251106089
CARD_MAP = {"V":10, "W":11, "X":12, "Y":13, "Z":14}
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')
    
    # replace symbols in order to describe value order between non single-digit cards
    processed=[(entry[0].replace("T","V").replace("J","W").replace("Q","X").replace("K","Y").replace("A","Z"), int(entry[1])) for entry in raw]

    return processed 

def determineType(hand):

    cardCounter = [0 for i in range(15)]

    pairCounter = 0
    for card in hand:
        if card in CARD_MAP:
            card = CARD_MAP[card]
        else:
            card = int(card)

        cardCounter[card]+=1 

        if cardCounter[card] == 2:
            pairCounter+=1


    # 0 - High
    # 1 - 2x
    # 2 - 2x2x
    # 3 - 3x
    # 4 - Full
    # 5 - 4x
    # 6 - 5x

    if 5 in cardCounter:
        return 6
    
    if 4 in cardCounter:
        return 5
    
    if 3 in cardCounter and 2 in cardCounter:
        return 4
    
    if 3 in cardCounter:
        return 3
    
    if pairCounter == 2:
        return 2
    
    if pairCounter == 1:
        return 1
    
    return 0

def solution(inputFile):
    result = 0
    
    games = getInputData(inputFile)

    types = [[] for i in range(7)]

    for game in games:
        hand = game[0]
        types[determineType(hand)].append(game)

    rank = 1
    for type in types:
        if type != []:
            type.sort(key=lambda e: e[0])
            for (hand,bid) in type:
                # log(rank,hand,bid)
                result += rank*bid
                rank += 1

    # log(types)

    log(red(250531843))
    return (result, EXPECTED_RESULT)