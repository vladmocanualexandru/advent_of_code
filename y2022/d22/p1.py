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

    map = matrixUtils.wrap(map, 'x', 1)

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
    # vizMap = []+map

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    # directionSymbols = ['>','v','<','^','O']

    directionIndex = 0
    height = len(map)
    width = len(map[0])

    posY = posX = -1

    for y in range(height):
        for x in range(width):
            if map[y][x] != 'x':
                posY = y
                posX = x
                break
        else:
            continue
        break

    # vizMap[posY][posX] = 'O'

    for step in path:
        if step == 'L':
            directionIndex=(directionIndex-1)%4

            # vizMap[posY][posX] = directionSymbols[directionIndex]
        elif step == 'R':
            directionIndex=(directionIndex+1)%4

            # vizMap[posY][posX] = directionSymbols[directionIndex]
        else:
            direction = directions[directionIndex]

            for stepCount in range(step):
                checkY = (posY+direction[0])%height
                checkX = (posX+direction[1])%width

                if map[checkY][checkX] == '#':
                    break

                if map[checkY][checkX] == 'x':
                    searchY = (checkY+direction[0])%height
                    searchX = (checkX+direction[1])%width

                    while map[searchY][searchX] == 'x':
                        searchY = (searchY+direction[0])%height
                        searchX = (searchX+direction[1])%width

                    if map[searchY][searchX] == '#':
                        break
                    else:
                        checkY = searchY
                        checkX = searchX

                posY = checkY
                posX = checkX

                # vizMap[posY][posX] = directionSymbols[directionIndex]

    # vizMap[posY][posX] = 'O'
    # logMatrix(vizMap, highlightElem=lambda e: red('x') if e == 'x' else (dark(C_BLOCK) if e == '#' else (green(e) if e in directionSymbols else ' ')))

    return 1000*posY+4*posX+directionIndex