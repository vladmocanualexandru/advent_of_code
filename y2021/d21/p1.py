import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_text(inputFile, 'position: ')

    return (int(raw[0][1]), int(raw[1][1]))


def solution(inputFile):
    inputData = getInputData(inputFile)

    player1 = inputData[0]-1
    player2 = inputData[1]-1

    score1 = score2 = 0

    # log('player1', player1)
    # log('player2', player2)

    track = [i for i in range(1,11)]
    die = [i for i in range(1,101)]

    # log(len(track), len(die))

    dieIndex = 0
    while score1<1000 and score2<1000:

        for i in range(3):
            player1 = (player1 + die[dieIndex%len(die)])%len(track)
            dieIndex+=1

        score1 += track[player1]

        # log(score1)


        if score1>=1000:
            # log('First player won!', score1, score2, dieIndex)

            return (score2*dieIndex,428736)

        
        for i in range(3):
            player2 = (player2 + die[dieIndex%len(die)])%len(track)
            dieIndex+=1

        score2 += track[player2]
        # log(score2)


        if score2>=1000:
            # log('Second player won!', score1, score2, dieIndex)

            return (score1*dieIndex,428736)


    return (-1,None)