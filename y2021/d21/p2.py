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
    GOAL = 21
    # TIMES = 3

    inputData = getInputData(inputFile)

    player1 = inputData[0]-1
    player2 = inputData[1]-1

    leaderboard = [0,0]

    track = [i for i in range(1,11)]

    # pips = [i for i in range(3,10)]

    pips = [3,4,5,6,7,8,9]
    pipValues = [0,0,0,1,3,6,7,6,3,1]

    def spawnUniverse(score1, position1, score2, position2, firstPlayerTurn, multiplier=1):


        # log(leaderboard)

        # if firstPlayerTurn:
        #     newPos = (position1+pip)%len(track)
        #     newScore = score1+track[newPos]
        #     if newScore>=GOAL:
        #         leaderboard[0]+=pipValues[pip]
        #         return
        # else:
        #     newPos = (position2+pip)%len(track)
        #     newScore = score2+track[newPos]
        #     if newScore>=GOAL:
        #         leaderboard[1]+=pipValues[pip]
        #         return

        if firstPlayerTurn:
            for pip in pips:
                newPos = (position1+pip)%len(track)
                newScore = score1+track[newPos]
                if newScore>=GOAL:
                    leaderboard[0]+=(multiplier*pipValues[pip])
                    continue
                else:
                    spawnUniverse(newScore, newPos, score2, position2, not firstPlayerTurn, multiplier*pipValues[pip] )
        else:
            for pip in pips:
                newPos = (position2+pip)%len(track)
                newScore = score2+track[newPos]
                if newScore>=GOAL:
                    leaderboard[1]+=(multiplier*pipValues[pip])
                    continue
                else:
                    spawnUniverse(score1, position1, newScore, newPos, not firstPlayerTurn, multiplier*pipValues[pip])


    
    spawnUniverse(0, player1, 0, player2, True)

    # log(outcome1[0]+outcome2[0]+outcome3[0],outcome1[1]+outcome2[1]+outcome3[1])

    return(leaderboard[0],57328067654557)