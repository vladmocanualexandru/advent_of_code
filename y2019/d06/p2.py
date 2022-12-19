import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 229

def getInputData(inputFile):
    raw = getTuples_text(inputFile,')')
    
    processed=[t[::-1] for t in raw]

    return processed 

def generateRouteToCOM(object, objects):
    result = [object]

    while object != 'COM':
        object = objects[object]
        result.append(object)

    return result

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    objects = {}

    for orbit in inputData:
        objects[orbit[0]] = orbit[1]

    myTransfers = generateRouteToCOM('YOU', objects)
    santasTransfers = generateRouteToCOM('SAN', objects)

    # log(myTransfers)
    # log(santasTransfers)

    result = 0
    for object in myTransfers:
        if object in santasTransfers:
            # log(green('Found common object %s' % object))

            youIndex = myTransfers.index(object)
            sanIndex = santasTransfers.index(object)

            # log('YOU common object index', youIndex)
            # log('SAN common object index', sanIndex)

            # 2 must be substracted because transfers are counted, not connections between YOU and SAN
            result = youIndex+sanIndex - 2
            break

    return (result,EXPECTED_RESULT)

 
