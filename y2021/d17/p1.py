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

    # xRange = [i for i in range(20, 31)]
    # yRange = [i for i in range(-10, -4)]    

    def getMaxY(vx, vy):
        x = y = 0

        maxY = 0
        while x<=xRange[-1] and y>=yRange[-1]:
            
            x+=vx
            y+=vy

            maxY = max(maxY, y)

            # log(y,x)

            if x in xRange and y in yRange:
                # log(vx,vy,'Good trajectory!')
                return maxY

            vx+=1 if vx<0 else (-1 if vx>0 else 0)
            vy-=1

            # input("")

        # log(vx,vy,'Bad trajectory!')
        return -1

    maxY = 0
    for vX in range(1,xRange[-1]+1):
        for vY in range(100,yRange[-1]-1, -1):
            maxY=max(maxY, getMaxY(vX, vY))

    return (maxY,3003)

 
