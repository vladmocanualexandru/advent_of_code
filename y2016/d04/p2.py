import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 548

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'-')
    
    processed=[parseRoom(room) for room in raw]

    return processed 

def parseRoom(room):
    tkns = room[-1].split('[')
    return [''.join(room[:-1]), int(tkns[0]), tkns[1][:-1]]

def decryptRoomName(roomName, sector):
    result = ''

    for c in roomName:
        result = result+string.ascii_lowercase[(string.ascii_lowercase.index(c)+sector)%len(string.ascii_lowercase)]

    return result

def solution(inputFile):
    input = getInputData(inputFile)

    for room in input:
        decryptedRoom = decryptRoomName(room[0], room[1])
        if 'north' in decryptedRoom:
            # log(decryptedRoom, room)
            result = room[1]

    return (result,EXPECTED_RESULT)

 