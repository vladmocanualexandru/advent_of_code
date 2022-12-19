import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,' players; last marble is worth ', ' points'])
    
    processed=(raw[0][0], raw[0][1])

    return processed 


def interweave(arr1,arr2):
    i1=i2=0
    result = []

    while i1<len(arr1) and i2<len(arr2):
        result.append(arr1[i1])
        result.append(arr2[i2])

        i1+=1
        i2+=1

    result += arr1[i1:]

    return (result

def solution(inputFile):
    inputData = getInputData(inputFile)

    log(inputData)


    # playerScores = [0 for i in range(inputData[0])]
    # marbles = [0,1]

    # playerTurn = 1
    # currentMarblePos = 1
    # for marbleValue in range(2, inputData[1]+1):
    #     if marbleValue % 23 == 0:
    #         seventhMarblePos = (currentMarblePos+len(marbles)-7)%len(marbles)
    #         playerScores[playerTurn] += marbleValue + marbles[seventhMarblePos]

    #         log(marbles[seventhMarblePos])

    #         marbles.remove(marbles[seventhMarblePos])
    #         currentMarblePos = seventhMarblePos%len(marbles)

    #         time.sleep(1)
    #     else:
    #         currentMarblePos = (currentMarblePos+2)%len(marbles)

    #         marbles[currentMarblePos:currentMarblePos] = [marbleValue]
        
    #     # log(playerTurn, marbles, "currentMarble=", marbles[currentMarblePos])

    #     playerTurn = (playerTurn + 1)%inputData[0]


    arr1 = [1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11]

    log("SCORE",23,arr1[14])
    del arr1[14]
    arr1 = arr1[15:]+arr1[:15]

    # log(arr1)
    # arr1 = interweave(arr1, [i for i in range(24,46)])
    # log(arr1)

    # times = 3200
    ballValue = 23
    
    playerScores = [0 for i in range(inputData[0])]
    playerIndex = 0
    playerScores[0]=32

    arr2 = []
    logLimit = 100000
    for ballValue in range(46, inputData[1], 23):

        if ballValue>logLimit:
            log(ballValue)
            logLimit+=100000

        # arr1 = interweave(arr1, [n for n in range(ballValue-23+1,ballValue)])

        arr1 = interweave(arr1, [n for n in range(ballValue-23+1,ballValue)])
        # arr1 = list(more_itertools.roundrobin(arr1, [n for n in range(ballValue-23+1,ballValue)]))
        playerIndex=(playerIndex+23)%inputData[0]
        playerScores[playerIndex] += ballValue+arr1[36]
        # log("SCORE",limit,arr1[36])
        del arr1[36]
        arr2 += arr1[:37]
        arr1 = arr1[37:]

        if len(arr1)<23:
            arr1+=arr2
            arr2 = []




    result = max(playerScores)



    # arr1 = interweave(arr1, [i for i in range(47,69)])
    # log("SCORE",69,arr1[36])
    # del arr1[36]
    # arr1 = arr1[37:]+arr1[:37]
    
    # arr1 = interweave(arr1, [i for i in range(70,92)])
    # log("SCORE",92,arr1[36])
    # del arr1[36]
    # arr1 = arr1[37:]+arr1[:37]

    # arr1 = interweave(arr1, [i for i in range(93,115)])
    # log("SCORE",115,arr1[36])
    # del arr1[36]
    # arr1 = arr1[37:]+arr1[:37]






    # 7th values:
    #   9
    #   17
    #   11
    #   15
    #   50
    #   58
    #   66
    #   33
    #   37
    #   99

    # arr1 = [1,3,0,4,2,5] 
    # arr2 = [6,7,8,9,10,11]
    # [1, 6, 3, 7, 0, 8, 4, 9, 2, 10, 5, 11]

    # arr1 = [1, 6, 3, 7, 0, 8, 4, 9, 2, 10, 5, 11]
    # arr2 = [12,13,14,15,16,17,18,19,20,21,22]

    # log(arr1)
    # log(arr2)
    # log(interweave(arr1,arr2))


    # currentIndex = 21
    # arr1 = [1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11]

    # currentIndex-=7
    # log('SCORE', 23, arr1[currentIndex])
    # log(arr1[currentIndex])

    # del arr1[currentIndex]

    # log(arr1[currentIndex])

    # log(arr1)
    # arr1 = arr1[currentIndex+1:]+arr1[:currentIndex+1]
    # log(arr1)
    # arr1 = interweave(arr1,[i for i in range(24,46)])

    # log(arr1)
    # log(max(arr1), len(arr1))

    # currentIndex=44-7
    # log('SCORE', 46, arr1[currentIndex])
    # del arr1[currentIndex]
    # arr1 = arr1[currentIndex+1:]+arr1[:currentIndex+1]
    # arr1 = interweave(arr1,[i for i in range(46,69)])

    # currentIndex=67-7
    # log('SCORE', 69, arr1[currentIndex])




    # arr3 = arr1+arr2

    # arr3[::2]=arr1
    # arr3[1::2]=arr2

    # log(arr3)

    return (result

 

