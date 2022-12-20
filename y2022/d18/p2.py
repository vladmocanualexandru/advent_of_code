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
    raw = getTuples_numbers(inputFile, ',')
    
    return raw 
    
def solution(inputFile):
    solidCubes = getInputData(inputFile)

    freeCubes = []
    trappedCubes = []

    # calculate space dimensions based on min/max of inpute data solidCubes' x,y,z coordinates
    minX = minY = minZ = pow(10,3)
    maxX = maxY = maxZ = -pow(10,3)

    for (x,y,z) in solidCubes:
        minX = min(minX, x)
        minY = min(minY, y)
        minZ = min(minZ, z)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        maxZ = max(maxZ, z)

    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            for z in range(minZ, maxZ+1):
                if not [x,y,z] in solidCubes:
                    trappedCubes.append([x,y,z])

    analysisDone = False
    while not analysisDone:
        analysisDone = True

        for [x,y,z] in []+trappedCubes:
            if x==minX or x==maxX or y==minY or y==maxY or z==minZ or z==maxZ:
                analysisDone = False
                trappedCubes.remove([x,y,z])
                freeCubes.append([x,y,z])
            else:
                if [x-1,y,z] in freeCubes or [x+1,y,z] in freeCubes or [x,y-1,z] in freeCubes or [x,y+1,z] in freeCubes or [x,y,z-1] in freeCubes or [x,y,z+1] in freeCubes:
                    analysisDone = False
                    trappedCubes.remove([x,y,z])
                    freeCubes.append([x,y,z])

    log(trappedCubes)

    log(red(2628, 2627, 1448, 1394, 1112))
    return None