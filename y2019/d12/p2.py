import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 277068010964808

MUN_COUNT = 4

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ', ')
    
    processed=[[int(entry[0].split('=')[1]), int(entry[1].split('=')[1]),  int(entry[2].split('=')[1][:-1])]  for entry in raw]
    processed=matrixUtils.flipMainDiagonal(processed)

    return processed 

def adjustVelocity(index1, index2, data):
    if data[index1]>data[index2]:
        data[index1+MUN_COUNT]-=1
        data[index2+MUN_COUNT]+=1
    elif data[index1]<data[index2]:
        data[index1+MUN_COUNT]+=1
        data[index2+MUN_COUNT]-=1

def solution(inputFile):
    initialCoords = getInputData(inputFile)

    targetX = initialCoords[0]+[0 for i in range(MUN_COUNT)]
    targetY = initialCoords[1]+[0 for i in range(MUN_COUNT)]
    targetZ = initialCoords[2]+[0 for i in range(MUN_COUNT)]

    x = targetX+[]
    y = targetY+[]
    z = targetZ+[]

    xCycle = yCycle = zCycle = -1
    iterCount = 0
    while xCycle == -1 or yCycle == -1 or zCycle == -1:
        for munIndex1 in range(MUN_COUNT-1):
            for munIndex2 in range(munIndex1+1, MUN_COUNT):
                if xCycle == -1:
                    adjustVelocity(munIndex1, munIndex2, x)
                if yCycle == -1:
                    adjustVelocity(munIndex1, munIndex2, y)
                if zCycle == -1:
                    adjustVelocity(munIndex1, munIndex2, z)

        for munIndex in range(MUN_COUNT):
            if xCycle == -1:
                x[munIndex]+=x[munIndex+MUN_COUNT]
            if yCycle == -1:
                y[munIndex]+=y[munIndex+MUN_COUNT]
            if zCycle == -1:
                z[munIndex]+=z[munIndex+MUN_COUNT]

        iterCount+=1

        if xCycle == -1 and x == targetX:
            xCycle = iterCount 

        if yCycle == -1 and y == targetY:
            yCycle = iterCount 
        
        if zCycle == -1 and z == targetZ:
            zCycle = iterCount 

    xDivs = numberUtils.splitIntoPrimeDivisors(xCycle)
    yDivs = numberUtils.splitIntoPrimeDivisors(yCycle)
    zDivs = numberUtils.splitIntoPrimeDivisors(zCycle)

    # log(xDivs)
    # log(yDivs)
    # log(zDivs)

    result = 1

    for d in xDivs:
        result *= d
        if d in yDivs:
            yDivs.remove(d)
        if d in zDivs:
            zDivs.remove(d)

    for d in yDivs:
        result *= d
        if d in zDivs:
            zDivs.remove(d)

    for d in zDivs:
        result *= d

    return (result,EXPECTED_RESULT)