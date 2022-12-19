import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

class Cave:
    name = 'unknown'
    isSmall = False
    visited = 0

    def __init__(self, name):
        self.name = name
        self.isSmall = name.islower()

    def __str__(self):
        return self.name

    def visit(self):
        self.visited+=1

class Connection :
    cave1=None
    cave2=None

    def __init__(self, cave1, cave2):
        self.cave1 = cave1
        self.cave2 = cave2

    def __str__(self):
        return '%s-%s' % (self.cave1.name, self.cave2.name)


def getInputData(inputFile):
    raw = getTuples_text(inputFile, '-')
    return raw

def getConnectedCaves(cave, connections):

    result = []
    for connection in connections:
        if connection.cave1 == cave:
            result.append(connection.cave2)
        elif connection.cave2 == cave:
            result.append(connection.cave1)

    return result

def travel(cave, viewedSmallCaveTwice, path, resultArray,connections):
  
    # log(cave.name)
    cave.visited += 1

    # log([str(c) for c in path])

    if cave.name == 'end':
        resultArray.append(1)
        # log('Path found!')
        return

    # log([str(c) for c in getConnectedCaves(cave)])


    for nextCave in getConnectedCaves(cave, connections):
        if nextCave.name == 'start':
            continue
        

        if nextCave.isSmall:
            if nextCave.visited>0:
                if not viewedSmallCaveTwice:
                    path.append(nextCave)
                    travel(nextCave, True, path, resultArray,connections)
                    path.pop(-1)

                    nextCave.visited-=1
                    continue
                else: 
                    continue
        
        path.append(nextCave)
        travel(nextCave, viewedSmallCaveTwice, path, resultArray,connections)
        path.pop(-1)

        nextCave.visited-=1

def solution(inputFile):

    inputData = getInputData(inputFile)

    caves = {}
    connections = []
    
    for connection in inputData:
        c1Name = connection[0]
        c2Name = connection[1]

        if not c1Name in caves:
            caves[c1Name] = Cave(c1Name)

        if not c2Name in caves:
            caves[c2Name] = Cave(c2Name)

        connections.append(Connection(caves[c1Name],caves[c2Name]))

    result = []
    travel(caves['start'], False, [], result,connections)

    return (sum(result),130493)
