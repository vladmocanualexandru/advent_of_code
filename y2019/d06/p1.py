import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 147807

def getInputData(inputFile):
    raw = getTuples_text(inputFile,')')
    
    processed=raw

    return processed 

def countOrbits(currentObject, objects, currentCount):
    objects[currentObject]["orbits"] = currentCount

    for object in objects[currentObject]["isOrbittedBy"]:
        countOrbits(object, objects, currentCount+1)

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[:10])

    objects = {}

    for orbit in inputData:
        if not orbit[0] in objects:
            objects[orbit[0]] = {"isOrbittedBy":[], "orbits":0}
        if not orbit[1] in objects:
            objects[orbit[1]] = {"isOrbittedBy":[], "orbits":0}

        objects[orbit[0]]["isOrbittedBy"].append(orbit[1])

    countOrbits("COM", objects, 0)

    # log(objects)

    result=sum([objects[o]["orbits"] for o in objects])

    return (result,EXPECTED_RESULT)

 
