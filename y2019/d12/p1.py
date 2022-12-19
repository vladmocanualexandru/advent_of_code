import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 6490

MUN_COUNT = 4
ITERATIONS = 1000

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

    x = initialCoords[0]+[0 for i in range(MUN_COUNT)]
    y = initialCoords[1]+[0 for i in range(MUN_COUNT)]
    z = initialCoords[2]+[0 for i in range(MUN_COUNT)]

    for iterCount in range(ITERATIONS):
        for munIndex1 in range(MUN_COUNT-1):
            for munIndex2 in range(munIndex1+1, MUN_COUNT):

                adjustVelocity(munIndex1, munIndex2, x)
                adjustVelocity(munIndex1, munIndex2, y)
                adjustVelocity(munIndex1, munIndex2, z)

        for munIndex in range(MUN_COUNT):
            x[munIndex]+=x[munIndex+MUN_COUNT]
            y[munIndex]+=y[munIndex+MUN_COUNT]
            z[munIndex]+=z[munIndex+MUN_COUNT]

    absValuesMat = matrixUtils.rotate(matrixUtils.apply([x,y,z], abs))
   
    result = 0
    for munIndex in range(MUN_COUNT):
        result+=sum(absValuesMat[munIndex])*sum(absValuesMat[munIndex+MUN_COUNT])

    return (result,EXPECTED_RESULT)