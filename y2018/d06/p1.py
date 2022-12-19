from random import random
import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 4060

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')

    minX = maxX = raw[0][0]
    minY = maxY = raw[0][1]

    for r in raw:
        minX = min(minX, r[0])
        minY = min(minY, r[1])
        maxX = max(maxX, r[0])
        maxY = max(maxY, r[1])

    processed=[(r[1]-minY, r[0]-minX) for r in raw]

    return (processed, maxY-minY+1, maxX-minX+1 ) 

def findClosestPoint(coord, points):
    closestNode = 'X'
    minDistance = pow(10,100)

    for label in points:
        point = points[label]
        if point[0] == coord[0] and point[1] == coord[1]:
            return label

        distance = abs(coord[0]-point[0]) + abs(coord[1]-point[1])
        if distance == minDistance:
            closestNode = '.'
        elif distance < minDistance:
            minDistance = distance
            closestNode= label

    return closestNode.lower()

def vizualize(e, infiniteLabels, finiteLabels, nodes, largestAreaLabel):
    if e == '.':
        return ' '
    elif e in nodes:
        return yellow(C_DOT_FULL)
    elif e == largestAreaLabel:
        return yellow(C_BLOCK)
    elif e in infiniteLabels:
        return red(C_BLOCK)
    elif e in finiteLabels:
        return formatOutput(nodes[e.upper()][2], C_BLOCK)
    else:
        return 'X'


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('input', inputData)

    matrix = matrixUtils.generate(inputData[1], inputData[2], '.')
    labels = ['%s0' % l for l in list(string.ascii_uppercase)]+['%s1' % l for l in list(string.ascii_uppercase)]+['%s2' % l for l in list(string.ascii_uppercase)]

    wrapSize = 0

    points = {}
    for i in range(len(inputData[0])):
        coord = inputData[0][i]
        matrix[coord[0]][coord[1]] = labels[i]

        points[labels[i]] = (coord[0]+wrapSize,coord[1]+wrapSize, [32,34,35,36][round(random()*3)])

    matrix = matrixUtils.wrap(matrix, '.', wrapSize)

    for lineI in range(len(matrix)):
        for colI in range(len(matrix[0])):
            closestNode = findClosestPoint((lineI, colI), points)
            matrix[lineI][colI] = closestNode


    # theory: areas that are on the outside are infinite
    infiniteAreaLabels = {}
    for elem in matrix[0]:
        if elem != '.':
            infiniteAreaLabels[elem] = True
    for elem in matrix[-1]:
        if elem != '.':
            infiniteAreaLabels[elem] = True
    for i in range(len(matrix)):
        if matrix[i][0] != '.':
            infiniteAreaLabels[matrix[i][0]] = True
        if matrix[i][-1] != '.':
            infiniteAreaLabels[matrix[i][-1]] = True

    finiteAreas = []
    finiteAreaLabels = {}
    for label in points:
        lowerLabel = label.lower()
        if not lowerLabel in infiniteAreaLabels:
            finiteAreas.append((lowerLabel, matrixUtils.addAll(matrix, lambda e: e==lowerLabel, lambda e: 1)+1)) 
            finiteAreaLabels[lowerLabel] = True
            # +1 because the coordinate label is uppercase and it's not counted, but it's relevant

    finiteAreas.sort(key=lambda e: e[1], reverse=True)

    # log(infiniteAreaLabels)
    # log(finiteAreaLabels)

    result = finiteAreas[0][1]

    # matrixUtils.log(matrix,'',log, lambda e: vizualize(e, infiniteAreaLabels, finiteAreaLabels, points, finiteAreas[0][0]))

    return (result,EXPECTED_RESULT)

 
