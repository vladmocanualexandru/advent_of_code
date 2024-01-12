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

EXPECTED_RESULT = 7185
 
def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    
    processed=[entry for entry in raw]

    return processed 

MOVEMENT = {
    "E" : {"yDelta":0, "xDelta":1},
    "S" : {"yDelta":1, "xDelta":0},
    "W" : {"yDelta":0, "xDelta":-1},
    "N" : {"yDelta":-1, "xDelta":0}
}

DIRECTION_LOGIC = {
    "E" : {".":"E", "|":"NS", "-":"E", "/":"N", "\\":"S"},
    "S" : {".":"S", "|":"S", "-":"EW", "/":"W", "\\":"E"},
    "W" : {".":"W", "|":"NS", "-":"W", "/":"S", "\\":"N"},
    "N" : {".":"N", "|":"N", "-":"EW", "/":"E", "\\":"W"}
}

def createRay(y,x,dir):
    return {"y":y, "x":x, "dir":dir}

def solution(inputFile):
    
    map = getInputData(inputFile)
    coverage = matrixUtils.generate(len(map),len(map[0]),'.')
    # surface = len(map) * len(map[0])

    map = matrixUtils.wrap(map, "x", 1)
    # coverage = matrixUtils.wrap(coverage, "x", 1)

    rays = [createRay(1,0,"E")]
    previousRays = []
    litPositions = []
    while len(rays)>0:
        newRays = []
        for ray in rays:
            # time.sleep(1)
            # log(red(ray), rays)
            ray["y"] += MOVEMENT[ray["dir"]]["yDelta"]
            ray["x"] += MOVEMENT[ray["dir"]]["xDelta"]
            # log(green(ray))

            if map[ray["y"]][ray["x"]] != 'x' and not ray in previousRays:
                previousRays.append(ray)
                for dir in DIRECTION_LOGIC[ray["dir"]][map[ray["y"]][ray["x"]]]:
                    newRays.append(createRay(ray["y"],ray["x"],dir))

                litPosition = (ray["y"], ray["x"])
                if not litPosition in litPositions:
                    litPositions.append(litPosition)
                # coverage[ray["y"]][ray["x"]] = 'o'

        rays = newRays

    result = len(litPositions)
    # logMatrix(map)
    # logMatrix(coverage)

    return (result, EXPECTED_RESULT)