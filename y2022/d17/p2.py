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
 
ROCK_COUNT = 1000000000000
# ROCK_COUNT =   1000000
# ROCK_COUNT =   2022

def getInputData(inputFile):
    raw = getText(inputFile)

    rocks = []

    rocks.append([(0,0),(0,1),(0,2),(0,3)])
    rocks.append([(0,1),(1,0),(1,1),(1,2),(2,1)])
    rocks.append([(0,2),(1,2),(2,0),(2,1),(2,2)])
    rocks.append([(0,0),(1,0),(2,0),(3,0)])
    rocks.append([(0,0),(0,1),(1,0),(1,1)])
    
    processed=(rocks, raw)

    return processed 

def solution(inputFile):
    (rocks, gusts) = getInputData(inputFile)

    # init cave
    cave = matrixUtils.generate(1, 9, '-')
    cave[0][0] = '+'
    cave[0][8] = '+'

    gustIndex = 0
    heightConfigs = []
    targetConfig = None
    prevRockIndex = None
    prevHeight = None
    jumpAhead = False
    finalHeight = 0

    # simulate ROCK_COUNT rocks
    rockIndex=-1
    while rockIndex < ROCK_COUNT:
        rockIndex+=1

        rockY = 0
        rockX = 3

        # create new rock at top
        rock = rocks[rockIndex%len(rocks)]
        for lineIndex in range(len(cave)):
            if cave[lineIndex]!=['|','.','.','.','.','.','.','.','|']:
                rockHeight = max([coord[0] for coord in rock])+1

                if (rockHeight+3-lineIndex)<0:
                    rockY=0-(rockHeight+3-lineIndex)
                cave = [['|','.','.','.','.','.','.','.','|'] for i in range(rockHeight+3-lineIndex)] + cave
                break

        # let rock settle
        rockSettled = False
        while not rockSettled:
            # apply wind gust
            gustValue = -1 if gusts[gustIndex] == '<' else 1
            gustIndex=(gustIndex+1)%len(gusts)
            
            for (coordY, coordX) in rock:
                if cave[rockY+coordY][rockX+coordX+gustValue] != '.':
                    break
            else:
                rockX+=gustValue

            # apply gravity
            for (coordY, coordX) in rock:
                if cave[rockY+coordY+1][rockX+coordX] != '.':
                    rockSettled = True
                    break
            else:
                rockY+=1

        # add rock to cave
        for (coordY, coordX) in rock:
            cave[rockY+coordY][rockX+coordX] = '#'

        if not jumpAhead:
            heightConfig = []
            for colIndex in range(1,8):
                for lineIndex in range(len(cave)-1):
                    if cave[lineIndex][colIndex] == '#':
                        heightConfig.append(lineIndex)
                        break

            heightConfig = [(max(heightConfig)+1-v) for v in heightConfig]+[rockIndex%len(rocks),gustIndex]

            if targetConfig == None:
                if heightConfig in heightConfigs:
                    log("Repetition detected!", heightConfig)
                    targetConfig = heightConfig
                else:
                    heightConfigs.append(heightConfig)
            elif heightConfig == targetConfig:
                height=0
                for lineIndex in range(len(cave)):
                    if cave[lineIndex]!=['|','.','.','.','.','.','.','.','|']:
                        height += (len(cave)-lineIndex)-1
                        break

                log("Target config found @rock",rockIndex,"height",height)
                if prevRockIndex == None:
                    prevRockIndex = rockIndex
                    prevHeight = height
                else:
                    rockDiff = rockIndex-prevRockIndex
                    heightDiff = height-prevHeight
                    log("Structure repeats every",rockDiff,"rocks and height is increased by",heightDiff)
                    jumpAheadSteps = math.floor((ROCK_COUNT-rockIndex)/rockDiff)
                    log("Jumping ahead by ",jumpAheadSteps,"steps")
                    rockIndex+=jumpAheadSteps*rockDiff
                    finalHeight=jumpAheadSteps*heightDiff
                    jumpAhead=True

    for lineIndex in range(len(cave)):
        if cave[lineIndex]!=['|','.','.','.','.','.','.','.','|']:
            finalHeight += (len(cave)-lineIndex)-1
            break

    return finalHeight-1