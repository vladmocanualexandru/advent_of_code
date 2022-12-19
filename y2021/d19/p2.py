import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def calculate3dDist(b1, b2):
    return math.sqrt(math.pow(b1.offsetX-b2.offsetX, 2)+math.pow(b1.offsetY-b2.offsetY, 2)+math.pow(b1.offsetZ-b2.offsetZ, 2))

def genDistanceIntersection(s1,s2):
    return list(set(s1.bDists) & set(s2.bDists))

class Beacon:
    def __init__(self, coordTuple):
        self.offsetX = int(coordTuple[0])
        self.offsetY = int(coordTuple[1])
        self.offsetZ = int(coordTuple[2])

    def __str__(self):
        return '%s/%s/%s' % (self.offsetX, self.offsetY, self.offsetZ)
    
    def __repr__(self):
        return '%s/%s/%s' % (self.offsetX, self.offsetY, self.offsetZ)

class Scanner:
    def __init__(self, scanner=None):
        self.beacons = []
        self.corrected = False

        if not scanner is None:
            self.bDists = [bd for bd in scanner.bDists]
            self.x = scanner.x
            self.y = scanner.y
            self.z = scanner.z
        else:
            self.bDists = []
            self.x = self.y = self.z = 0

    def addBeacon(self, coordTuple):
        self.beacons.append(Beacon(coordTuple))

        for beacon in self.beacons[:-1]:
            dist = calculate3dDist(beacon, self.beacons[-1])
            self.bDists.append(dist)

    def __str__(self):
        return 'beacons(%s)=%s, bDists=%s' % (len(self.beacons), self.beacons, self.bDists)

    def __repr__(self):
        return 'beacons(%s)=%s, bDists=%s' % (len(self.beacons), self.beacons, self.bDists)

def getInputData(inputFile):
    raw = getStrings(inputFile)

    scanners = []
    for line in raw:
        if line=='': 
            continue

        if not ',' in line:
            scanners.append(Scanner())
        else:
            scanners[-1].addBeacon(line.split(','))
    
    return scanners


def solution(inputFile):
    scanners = getInputData(inputFile)

    def rotate(translationIndex, scanner):
        result = Scanner(scanner)

        if translationIndex == -1:
            return scanner
        elif translationIndex == 0:
            result.beacons = [Beacon((b.offsetX,b.offsetZ,-b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 1:
            result.beacons = [Beacon((b.offsetX,-b.offsetY,-b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 2:
            result.beacons = [Beacon((b.offsetX,-b.offsetZ,b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 3:
            result.beacons = [Beacon((-b.offsetX,-b.offsetY,b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 4:
            result.beacons = [Beacon((-b.offsetX,b.offsetZ,b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 5:
            result.beacons = [Beacon((-b.offsetX,b.offsetY,-b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 6:
            result.beacons = [Beacon((-b.offsetX,-b.offsetZ,-b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 7:
            result.beacons = [Beacon((b.offsetY,b.offsetZ,b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 8:
            result.beacons = [Beacon((b.offsetY,b.offsetX,-b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 9:
            result.beacons = [Beacon((b.offsetY,-b.offsetZ,-b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 10:
            result.beacons = [Beacon((b.offsetY,-b.offsetX,b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 11:
            result.beacons = [Beacon((-b.offsetY,-b.offsetZ,b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 12:
            result.beacons = [Beacon((-b.offsetY,b.offsetX,b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 13:
            result.beacons = [Beacon((-b.offsetY,b.offsetZ,-b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 14:
            result.beacons = [Beacon((-b.offsetY,-b.offsetX,-b.offsetZ)) for b in scanner.beacons]
        elif translationIndex == 15:
            result.beacons = [Beacon((b.offsetZ,b.offsetX,b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 16:
            result.beacons = [Beacon((b.offsetZ,b.offsetY,-b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 17:
            result.beacons = [Beacon((b.offsetZ,-b.offsetX,-b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 18:
            result.beacons = [Beacon((b.offsetZ,-b.offsetY,b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 19:
            result.beacons = [Beacon((-b.offsetZ,-b.offsetX,b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 20:
            result.beacons = [Beacon((-b.offsetZ,b.offsetY,b.offsetX)) for b in scanner.beacons]
        elif translationIndex == 21:
            result.beacons = [Beacon((-b.offsetZ,b.offsetX,-b.offsetY)) for b in scanner.beacons]
        elif translationIndex == 22:
            result.beacons = [Beacon((-b.offsetZ,-b.offsetY,-b.offsetX)) for b in scanner.beacons]

        return result
    
    def translate(scanner, deltaX, deltaY, deltaZ):
        result = Scanner(scanner)

        result.beacons = [Beacon((b.offsetX+deltaX, b.offsetY+deltaY, b.offsetZ+deltaZ)) for b in scanner.beacons]
        result.x=deltaX
        result.y=deltaY
        result.z=deltaZ

        return result

    def calculateAllDistances(s1,s2):
        result = {}

        for b1 in s1.beacons:
            for b2 in s2.beacons:
                distance = str(calculate3dDist(b1,b2))
                if not distance in result:
                    result[distance] = (0, b1, b2)

                result[distance] = (result[distance][0]+1, b1, b2)
        return result

    def maxDistanceCount(distances):
        maxCount = -1
        b1 = None
        b2 = None

        for distance in distances:
            if maxCount < distances[distance][0]:
                maxCount = distances[distance][0]
                b1 = distances[distance][1]
                b2 = distances[distance][2]

        return (maxCount,b1,b2)

    scanners[0].corrected=True

    allScannersCorrected=False
    while(not allScannersCorrected):
        allScannersCorrected = True

        for i in range(len(scanners)):
            scanner1 = scanners[i]
            if not scanner1.corrected:
                allScannersCorrected = False
                continue
            else:
                for j in range(len(scanners)):
                    scanner2= scanners[j]
                    if scanner2.corrected == False and len(genDistanceIntersection(scanner1,scanner2))==66:
                        allScannersCorrected = False

                        for translationIndex in range(-1,23):
                            newScanner = rotate(translationIndex,scanner2)
                            maxInfo = maxDistanceCount(calculateAllDistances(scanner1, newScanner))

                            if (maxInfo[0]>=12):
                                scanners[j] = translate(
                                    newScanner, 
                                    maxInfo[1].offsetX-maxInfo[2].offsetX,
                                    maxInfo[1].offsetY-maxInfo[2].offsetY,
                                    maxInfo[1].offsetZ-maxInfo[2].offsetZ)

                                scanners[j].corrected = True

                                break

    
    maxManhattanDistance = -1

    for s1 in scanners:
        for s2 in scanners:
            # log(s1.x, s1.y, s1.z)
            # log(s2.x, s2.y, s2.z)
            # log('----------------------------------')
            maxManhattanDistance = max(maxManhattanDistance,abs(s1.x-s2.x)+abs(s1.y-s2.y)+abs(s1.z-s2.z))


    result = maxManhattanDistance

    return (result,12317)

 
