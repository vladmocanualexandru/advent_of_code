import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 14687245

MAGNITUDE=1000

def getInputData(inputFile):
    raw = getTuples_text(inputFile)

    processed = []

    for rawTuple in raw:
        processed.append([rawTuple[0], extractCoords(rawTuple[1]), extractCoords(rawTuple[3])])

    return processed

def extractCoords(coordString):
    tkns = coordString.split(',')
    return [int(tkns[0]), int(tkns[1])]

def convertCoordsToIndex(coords):
    return coords[0]*MAGNITUDE+coords[1]

def computeAreaCoords(fromCoord, toCoord):
    coords = []

    coord = []+fromCoord
    while coord[0]!=toCoord[0] or coord[1] != toCoord[1]:
        coords.append(convertCoordsToIndex(coord))

        if coord[1]==toCoord[1]:
            coord[0]+=1
            coord[1]=fromCoord[1]
        else:
            coord[1]+=1
        
    coords.append(convertCoordsToIndex(toCoord))

    return coords

def handleCommand(board, command):

    targetCoords = computeAreaCoords(command[1], command[2])

    for coord in targetCoords:
        if command[0] == 'turn_on':
            board[coord] += 1
        elif command[0] == 'turn_off':
            board[coord] = max(0, board[coord]-1)
        else:
            board[coord] += 2

def solution(inputFile):
    inputData = getInputData(inputFile)
    board = [0 for a in range(pow(MAGNITUDE,2))]

    for command in inputData:
        handleCommand(board, command)

    # for lineIndex in range(0,len(board), MAGNITUDE):
    #     print(board[lineIndex:lineIndex+MAGNITUDE])

    result = sum(board)

    return (result, EXPECTED_RESULT)

 