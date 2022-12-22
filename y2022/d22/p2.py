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

# # EXAMPLE DATA

# MAP_WIDTH_TILES = 4
# MAP_HEIGHT_TILES = 3

# FACE_A_COORDS = (0,2)
# FACE_B_COORDS = (1,0)
# FACE_C_COORDS = (1,1)
# FACE_D_COORDS = (1,2)
# FACE_E_COORDS = (2,2)
# FACE_F_COORDS = (2,3)

# DIRECTION_MAPPING={
#     ("A","E"):{"face":"F", "direction":"W", "reverseX":False, "reverseY":True, "flipCoords":False},
#     ("A","S"):{"face":"D", "direction":"S", "reverseX":False, "reverseY":True, "flipCoords":False},
#     ("A","W"):{"face":"C", "direction":"S", "reverseX":False, "reverseY":False, "flipCoords":True},
#     ("A","N"):{"face":"B", "direction":"S", "reverseX":True, "reverseY":False, "flipCoords":False},

#     ("B","E"):{"face":"C", "direction":"E", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("B","S"):{"face":"E", "direction":"N", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("B","W"):{"face":"F", "direction":"N", "reverseX":True, "reverseY":True, "flipCoords":True},
#     ("B","N"):{"face":"A", "direction":"S", "reverseX":True, "reverseY":False, "flipCoords":False},

#     ("C","E"):{"face":"D", "direction":"E", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("C","S"):{"face":"E", "direction":"E", "reverseX":True, "reverseY":True, "flipCoords":True},
#     ("C","W"):{"face":"B", "direction":"W", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("C","N"):{"face":"A", "direction":"E", "reverseX":False, "reverseY":False, "flipCoords":True},

#     ("D","E"):{"face":"F", "direction":"S", "reverseX":True, "reverseY":True, "flipCoords":True},
#     ("D","S"):{"face":"E", "direction":"S", "reverseX":False, "reverseY":True, "flipCoords":False},
#     ("D","W"):{"face":"C", "direction":"W", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("D","N"):{"face":"A", "direction":"N", "reverseX":False, "reverseY":True, "flipCoords":False},

#     ("E","E"):{"face":"F", "direction":"E", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("E","S"):{"face":"B", "direction":"N", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("E","W"):{"face":"C", "direction":"N", "reverseX":True, "reverseY":True, "flipCoords":True},
#     ("E","N"):{"face":"D", "direction":"N", "reverseX":False, "reverseY":True, "flipCoords":False},

#     ("F","E"):{"face":"A", "direction":"W", "reverseX":False, "reverseY":True, "flipCoords":False},
#     ("F","S"):{"face":"B", "direction":"E", "reverseX":True, "reverseY":True, "flipCoords":True},
#     ("F","W"):{"face":"E", "direction":"W", "reverseX":True, "reverseY":False, "flipCoords":False},
#     ("F","N"):{"face":"D", "direction":"W", "reverseX":True, "reverseY":True, "flipCoords":True},
# }

# TEST DATA - CONFIGURATION IS CUSTOM TAILORED TO INPUT DATA
MAP_WIDTH_TILES = 3
MAP_HEIGHT_TILES = 4

FACE_A_COORDS = (0,1)
FACE_B_COORDS = (0,2)
FACE_C_COORDS = (1,1)
FACE_D_COORDS = (2,0)
FACE_E_COORDS = (2,1)
FACE_F_COORDS = (3,0)

DIRECTION_MAPPING={
    ("A","E"):{"face":"B", "direction":"E", "reverseX":True, "reverseY":False, "flipCoords":False},
    ("A","S"):{"face":"C", "direction":"S", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("A","W"):{"face":"D", "direction":"E", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("A","N"):{"face":"F", "direction":"E", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("B","E"):{"face":"E", "direction":"W", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("B","S"):{"face":"C", "direction":"W", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("B","W"):{"face":"A", "direction":"W", "reverseX":True, "reverseY":False, "flipCoords":False},
    ("B","N"):{"face":"F", "direction":"N", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("C","E"):{"face":"B", "direction":"N", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("C","S"):{"face":"E", "direction":"S", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("C","W"):{"face":"D", "direction":"S", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("C","N"):{"face":"A", "direction":"N", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("D","E"):{"face":"E", "direction":"E", "reverseX":True, "reverseY":False, "flipCoords":False},
    ("D","S"):{"face":"F", "direction":"S", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("D","W"):{"face":"A", "direction":"E", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("D","N"):{"face":"C", "direction":"E", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("E","E"):{"face":"B", "direction":"W", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("E","S"):{"face":"F", "direction":"W", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("E","W"):{"face":"D", "direction":"W", "reverseX":True, "reverseY":False, "flipCoords":False},
    ("E","N"):{"face":"C", "direction":"N", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("F","E"):{"face":"E", "direction":"N", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("F","S"):{"face":"B", "direction":"S", "reverseX":False, "reverseY":True, "flipCoords":False},
    ("F","W"):{"face":"A", "direction":"S", "reverseX":False, "reverseY":False, "flipCoords":True},
    ("F","N"):{"face":"D", "direction":"N", "reverseX":False, "reverseY":True, "flipCoords":False},
}

FACE_RATIO={
    "A":FACE_A_COORDS,
    "B":FACE_B_COORDS,
    "C":FACE_C_COORDS,
    "D":FACE_D_COORDS,
    "E":FACE_E_COORDS,
    "F":FACE_F_COORDS
}

def getNextTransFaceMove(y, x, currentFace, direction, faces, tileSize):
    moveData = DIRECTION_MAPPING[(currentFace, direction)]

    if moveData["reverseY"]:
        y = tileSize-y-1
    if moveData["reverseX"]:
        x = tileSize-x-1

    y = max(0,min(y,tileSize-1))
    x = max(0,min(x,tileSize-1))

    if moveData["flipCoords"]:
        (y,x)=(x,y)

    return {"face":moveData["face"], "direction":moveData["direction"], "y":y, "x":x}

 
def getInputData(inputFile):
    raw = getRawLines(inputFile)

    rawMap= raw[:-2]

    maxWidth = max([len(line) for line in rawMap])-1
    map = matrixUtils.generate(len(rawMap), maxWidth, 'x')

    for lineIndex in range(len(rawMap)):
        line = rawMap[lineIndex][:-1]
        for colIndex in range(len(line)):
            if line[colIndex] in ['.',"#"]:
                map[lineIndex][colIndex] = line[colIndex]

    path = []
    pathString = raw[-1].strip()
    oldCharIndex = 0
    for charIndex in range(len(pathString)):
        if pathString[charIndex] in ['L','R']:
            path.append(int(pathString[oldCharIndex:charIndex]))
            path.append(pathString[charIndex])
            oldCharIndex=charIndex+1

    path.append(int(pathString[oldCharIndex:]))

    return (map, path) 

def solution(inputFile):
    (map, path) = getInputData(inputFile)
    
    tileSize = int(len(map)/MAP_HEIGHT_TILES)

    faces = {
        "A":[line[tileSize*FACE_A_COORDS[1]:tileSize*(FACE_A_COORDS[1]+1)]  for line in map[tileSize*FACE_A_COORDS[0]:tileSize*(FACE_A_COORDS[0]+1)]],
        "B":[line[tileSize*FACE_B_COORDS[1]:tileSize*(FACE_B_COORDS[1]+1)]  for line in map[tileSize*FACE_B_COORDS[0]:tileSize*(FACE_B_COORDS[0]+1)]],
        "C":[line[tileSize*FACE_C_COORDS[1]:tileSize*(FACE_C_COORDS[1]+1)]  for line in map[tileSize*FACE_C_COORDS[0]:tileSize*(FACE_C_COORDS[0]+1)]],
        "D":[line[tileSize*FACE_D_COORDS[1]:tileSize*(FACE_D_COORDS[1]+1)]  for line in map[tileSize*FACE_D_COORDS[0]:tileSize*(FACE_D_COORDS[0]+1)]],
        "E":[line[tileSize*FACE_E_COORDS[1]:tileSize*(FACE_E_COORDS[1]+1)]  for line in map[tileSize*FACE_E_COORDS[0]:tileSize*(FACE_E_COORDS[0]+1)]],
        "F":[line[tileSize*FACE_F_COORDS[1]:tileSize*(FACE_F_COORDS[1]+1)]  for line in map[tileSize*FACE_F_COORDS[0]:tileSize*(FACE_F_COORDS[0]+1)]],
    }

    directionSymbols = ["E", "S", "W", "N"]
    directions = {"E":(0,1),"S":(1,0),"W":(0,-1),"N":(-1,0)}

    direction = "E"
    currentFace = "A"
    posY = posX = 0


    direction = "E"
    currentFace = "A"
    posY = posX = 0

    for step in path:
        if step == 'L':
            directionIndex = directionSymbols.index(direction)
            directionIndex = (directionIndex-1)%4
            direction = directionSymbols[directionIndex]
        elif step =='R':
            directionIndex = directionSymbols.index(direction)
            directionIndex = (directionIndex+1)%4
            direction = directionSymbols[directionIndex]
        else:
            for stepCounter in range(step):
                directionData = directions[direction]
                checkY = posY+directionData[0]
                checkX = posX+directionData[1]

                if checkY<0 or checkY==tileSize or checkX<0 or checkX==tileSize:
                    nextFaceData = getNextTransFaceMove(checkY, checkX, currentFace, direction, faces, tileSize)
                    if faces[nextFaceData["face"]][nextFaceData["y"]][nextFaceData["x"]] == '.':
                        checkY = nextFaceData["y"]
                        checkX = nextFaceData["x"]
                        currentFace = nextFaceData["face"]
                        direction = nextFaceData["direction"]
                    else:
                        break
                elif faces[currentFace][checkY][checkX] == '#':
                        break

                posY = checkY
                posX = checkX

    result = (FACE_RATIO[currentFace][0]*tileSize+posY+1)*1000
    result += (FACE_RATIO[currentFace][1]*tileSize+posX+1)*4
    result += directionSymbols.index(direction)

    return result