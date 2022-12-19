import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 436720

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,' players; last marble is worth ', ' points')
    
    processed=(raw[0][0], raw[0][1])

    return processed 


def solution(inputFile):
    inputData = getInputData(inputFile)

    playerScores = [0 for i in range(inputData[0])]
    marbles = [0,1]

    playerTurn = 1
    currentMarblePos = 1
    for marbleValue in range(2, inputData[1]+1):
        if marbleValue % 23 == 0:
            seventhMarblePos = (currentMarblePos+len(marbles)-7)%len(marbles)
            playerScores[playerTurn] += marbleValue + marbles[seventhMarblePos]

            marbles.remove(marbles[seventhMarblePos])
            currentMarblePos = seventhMarblePos%len(marbles)
        else:
            currentMarblePos = (currentMarblePos+2)%len(marbles)

            marbles[currentMarblePos:currentMarblePos] = [marbleValue]
        
        # log(playerTurn, marbles, "currentMarble=", marbles[currentMarblePos])

        playerTurn = (playerTurn + 1)%inputData[0]


    # log(playerScores)

    result=max(playerScores)
    return (result,EXPECTED_RESULT)

 

