import sys, os, math, numpy

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 1623

ANGLE_PRECISION = 4

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'')
    
    processed=raw

    return processed 

def getDistance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def solution(inputFile):
    matrix = getInputData(inputFile)
    

    stationLocation = (28,22)
    # stationLocation = (13,11)
    # stationLocation = (6,3)
    # stationLocation = (3,8)
    # stationLocation = (4,3)

    matrix[stationLocation[0]][stationLocation[1]] = 'O'

    points = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '#':
                points.append((y-stationLocation[0],x-stationLocation[1]))

    # from this point on, the station location is the reference 0,0 location

    # matrixUtils.log(matrix, '', log, lambda e: light(e) if e == 'O' else 'x' if e == '#' else '.')
    # log(points)

    angles = {}
    for point in points:
 
        angle = None
        dist = getDistance((0,0), point)
        if point[1]>=0:
            angle = 180-numpy.arccos(point[0]/dist)*(180/math.pi)
        else:
            angle = 180+numpy.arccos(point[0]/dist)*(180/math.pi)

        angle = round(angle,ANGLE_PRECISION)

        if not angle in angles:
            angles[angle] = []

        # with this occasion the asteroid locations are translated back to their original values
        angles[angle].append(((point[0]+stationLocation[0], point[1]+stationLocation[1]), dist))

    flatAngles = []
    for angle in angles:
        points = angles[angle]

        points.sort(key = lambda x: x[1])

        for multiplier in range(len(points)):
            flatAngles.append((angle+multiplier*360, points[multiplier][0]))


    flatAngles.sort(key = lambda x: x[0])

    # vizualization

    # for flatAngle in flatAngles:
    #     multi360 = math.floor(flatAngle[0]/360)
    #     if multi360==3:
    #         break

    #     matrix[flatAngle[1][0]][flatAngle[1][1]] = multi360

    # matrixUtils.log(matrix, '', log, lambda e: light(C_DOT_FULL) if e == 'O' else red('x') if e == 0 else green('x') if e == 1 else blue('x') if e == 2 else C_DOT_TRANSPARENT if e == '#' else ' ')
    # matrixUtils.log(matrix, '', log, lambda e: light(C_DOT_FULL) if e == 'O' else C_DOT_TRANSPARENT if e not in [0,1,2,'.'] else ' ')

    # log(flatAngles)

    pointNo200 = flatAngles[199][1]

    result = pointNo200[1]*100+pointNo200[0]
    return (result,EXPECTED_RESULT)

 

