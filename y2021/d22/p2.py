import sys, os, random

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

# for cuboid:
#     - add volume
#     - substract intersection with cuboids
#     - add intersection of substracted intersections

class Cuboid:
    def __init__(self, limits, type):
        self.type = type
        self.limits = {}

        self.minX = limits[0]
        self.maxX = limits[1]
        self.minY = limits[2]
        self.maxY = limits[3]
        self.minZ = limits[4]
        self.maxZ = limits[5]

    def getVolume(self):
        return (self.maxX-self.minX+1)*(self.maxY-self.minY+1)*(self.maxZ-self.minZ+1)

    def __str__(self):
        return "%s, x=%d..%d,y=%d..%d,z=%d..%d" % (self.type, self.minX, self.maxX, self.minY, self.maxY, self.minZ, self.maxZ)

    def __repr__(self):
        return self.__str__()



def getInputData(inputFile):
    raw = getTuples_text(inputFile,  ' x=', '..', ',y=', ',z=')
    
    processed=[]

    for entry in raw:
        cuboid = Cuboid([int(e) for e in entry[1:]], entry[0])
        processed.append(cuboid)

    return processed

def calculateIntersection(cuboid1, cuboid2, type):
    if cuboid1.minX > cuboid2.maxX or cuboid1.maxX < cuboid2.minX or cuboid1.minY > cuboid2.maxY or cuboid1.maxY < cuboid2.minY or cuboid1.minZ > cuboid2.maxZ or cuboid1.maxZ < cuboid2.minZ:
        return []
    else:
        intC = Cuboid([0 for i in range(6)], type)
        intC.minX = max(cuboid1.minX, cuboid2.minX)
        intC.maxX = min(cuboid1.maxX, cuboid2.maxX)
        intC.minY = max(cuboid1.minY, cuboid2.minY)
        intC.maxY = min(cuboid1.maxY, cuboid2.maxY)
        intC.minZ = max(cuboid1.minZ, cuboid2.minZ)
        intC.maxZ = min(cuboid1.maxZ, cuboid2.maxZ)
        return [intC]

     

def solution(inputFile):
    inputData = getInputData(inputFile)

    cuboids = []

    for i in range(len(inputData)):
        # log('%0.2f' % (i/len(inputData)*100))
        cuboidInfo = inputData[i]

        newCuboids = []
        for cuboid in cuboids:
            newCuboids += calculateIntersection(cuboidInfo, cuboid, 'off' if cuboid.type == 'on' else 'on')
        cuboids += newCuboids

        if cuboidInfo.type == 'on':
            cuboids.append(cuboidInfo)

    # log(cuboids)

    result=sum([c.getVolume() if c.type=='on' else -c.getVolume() for c in cuboids])

    return (result,1160011199157381)