import sys, os

from more_itertools import interleave

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

    # arr = [11,  1, 12,  6, 13,  3, 14,  7, 15, 0, 16,  8, 17,  4, 18,  9, 19,  2, 20, 10, 21,  5, 22]
    # log("SCORE", 23, arr[-8])

    # del arr[-8]
    # arr = interweave(arr[-6:]+arr[0:-6], [n for n in range(24,46)])
    # log("SCORE", 46, arr[36])

    # log(arr)

    log("SCORE", 23, 9, "(static)")
    log("SCORE",  46, 17, "(static)")

    arr = [2, 24, 20, 25, 10, 26, 21, 27, 5, 28, 22, 29, 11, 30, 1, 31, 12, 32, 6, 33, 13, 34, 3, 35, 14, 36, 7, 37, 15, 38, 0, 39, 16, 40, 8, 41, 17, 42, 4, 43, 18, 44, 19, 45]

    # del arr[36]
    # arr = interweave(arr[37:]+arr[0:37], [n for n in range(47,69)])
    # log("SCORE", 69, arr[36])

    # del arr[36]
    # arr = interweave(arr[37:]+arr[0:37], [n for n in range(70,92)])
    # log("SCORE", 92, arr[36])

    # del arr[36]
    # arr = interweave(arr[37:]+arr[0:37], [n for n in range(93,115)])
    # log("SCORE", 115, arr[36])

    # del arr[36]
    # arr = interweave(arr[37:]+arr[0:37], [n for n in range(116,138)])
    # log("SCORE", 138, arr[36])

    playerScores = [0 for n in range(inputData[0])]

    playerScores[0] = 32
    playerIndex = 23%inputData[0]
    playerScores[playerIndex] = 40

    for marbleValue in range(69, inputData[1]+1, 23):
        del arr[36]
        arr = interweave(arr[37:]+arr[0:37], [n for n in range(marbleValue-22,marbleValue)])

        playerIndex = (playerIndex + 23)%inputData[0]
        playerScores[playerIndex]+=marbleValue + arr[36]
        log("SCORE", marbleValue, arr[36])

        # time.sleep(0.2)

    result = max(playerScores)
    return (result

 

