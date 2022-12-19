import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = [t.split('..') for t in getTuples_text(inputFile, ', ')[0]]

    xTuple = (int(raw[0][0][15:]), int(raw[0][1]))
    yTuple = (int(raw[1][0][2:]), int(raw[1][1]))

    return [[i for i in range(xTuple[0], xTuple[1]+1)], [i for i in range(yTuple[0], yTuple[1]+1)]]


def solution(inputFile):
    inputData = getInputData(inputFile)

    xRange = inputData[0]
    yRange = inputData[1]

    def isGoodTrajectory(vx, vy):
        x = y = 0
        while x<=xRange[-1] and y>=yRange[0]:
            
            x+=vx
            y+=vy

            if x in xRange and y in yRange:
                return True

            vx+=1 if vx<0 else (-1 if vx>0 else 0)
            vy-=1

        return False

    trajectories = set()
    for vX in range(1,xRange[-1]+10):
        for vY in range(150,yRange[0]-10, -1):
            if isGoodTrajectory(vX, vY):
                trajectories.add((vX, vY))

    return (len(trajectories),940)

 
