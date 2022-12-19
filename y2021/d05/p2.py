import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 


RESOLUTION = 1000

def updateDiagramUnit(diagram, index):
    diagram[index] = min(diagram[index]+1, 1)

def updateDiagram(diagram, startPos, stopPos):

    indexes = [startPos[0]*RESOLUTION + startPos[1] , stopPos[0]*RESOLUTION + stopPos[1]]
    indexes.sort()

    delta = 0
    if startPos[0]!=stopPos[0]:
        delta = RESOLUTION

    if indexes[0]%RESOLUTION<indexes[1]%RESOLUTION:
        delta+=1
    elif indexes[0]%RESOLUTION>indexes[1]%RESOLUTION:
        delta-=1

    for index in range(indexes[0]+delta, indexes[1], delta):
        updateDiagramUnit(diagram, index)

    updateDiagramUnit(diagram, indexes[0])
    updateDiagramUnit(diagram, indexes[1])

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' -> ')
    
    processed=[[[int(a) for a in rawTuple[0].split(',')], [int(b) for b in rawTuple[1].split(',')]] for rawTuple in raw]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)

    # input = [['0,9','5,9']
    # ,['8,0','0,8']
    # ,['9,4','3,4']
    # ,['2,2','2,1']
    # ,['7,0','7,4']
    # ,['6,4','2,0']
    # ,['0,9','2,9']
    # ,['3,4','1,4']
    # ,['0,0','8,8']
    # ,['5,5','8,2']]

    diagram  = []

    for i in range(pow(RESOLUTION,2)):
        diagram.append(-1)

    for vent in input:
        updateDiagram(diagram, vent[0], vent[1])

    result = sum(unit for unit in diagram if unit==1)

    return (result,19349)