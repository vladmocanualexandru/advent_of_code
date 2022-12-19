from dis import dis
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 56410

MATRIX_SIZE = 18

def getInputData(inputFile):
    raw = getTuples_text(inputFile,',')
    
    processed=[]
    for tuple in raw:
        wire = []
        for coord in tuple:
            wire.append((coord[0],int(coord[1:])))
        processed.append(wire)

    return processed 

def generateWire(data):
    pos = (0,0)
    segments = []

    for coord in data:
        direction = coord[0]

        newPos = (pos[0], pos[1] + coord[1])

        if direction == 'L':
            newPos = (pos[0], pos[1]-coord[1])
        elif direction == 'U':
            newPos = (pos[0]-coord[1], pos[1])
        elif direction == 'D':
            newPos = (pos[0]+coord[1], pos[1])

        segments.append((pos, newPos))

        pos = (newPos[0], newPos[1])

    return segments

def calculateIntersection(intervalA, intervalB):

    horizSegment = None
    vertSegment = None

    if intervalA[0][0] == intervalA[1][0]: 
        horizSegment = intervalA
    else:
        vertSegment = intervalA

    if intervalB[0][0] == intervalB[1][0]: 
        horizSegment = intervalB
    else:
        vertSegment = intervalB

    if not horizSegment or not vertSegment:
        return None

    fixedY = horizSegment[0][0]
    fixedX = vertSegment[0][1]

    if fixedY<min(vertSegment[0][0], vertSegment[1][0]) or fixedY>max(vertSegment[0][0], vertSegment[1][0]):
        return None

    if fixedX<min(horizSegment[0][1], horizSegment[1][1]) or fixedX>max(horizSegment[0][1], horizSegment[1][1]):
        return None

    return (fixedY, fixedX)

def pointOnSegment(segment, point):
    result = point[0] >= min(segment[0][0], segment[1][0]) and point[0] <= max(segment[0][0], segment[1][0])
    result = result and point[1] >= min(segment[0][1], segment[1][1]) and point[1] <= max(segment[0][1], segment[1][1])

    return result

def calculateSegmentLength(pointA, pointB):
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])

def calculateWireDistanceTo(wire, point):

    distance = 0
    for segment in wire:
        if not pointOnSegment(segment, point):
            distance += calculateSegmentLength(segment[0], segment[1])
        else:
            distance += calculateSegmentLength(segment[0], point)
            break

    return distance
    
def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    wire0 = generateWire(inputData[0])
    # log('wire 0 generated')
    
    wire1 = generateWire(inputData[1])
    # log('wire 1 generated')

    intersections = []
    for interval0 in wire0:
        for interval1 in wire1:
            intersection = calculateIntersection(interval0, interval1)
            if not intersection is None and (intersection[0]!=0 or intersection[1]!=0):
                intersections.append(intersection)

    result = min([calculateWireDistanceTo(wire0, iPoint)+calculateWireDistanceTo(wire1, iPoint) for iPoint in intersections])

    return (result,EXPECTED_RESULT)

 
