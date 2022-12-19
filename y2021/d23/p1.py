from logging.handlers import WatchedFileHandler
import sys, os, time, random

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

LOCATIONS = ['a0','a1','b0','b1','c0','c1','d0','d1','h0','h1','h2','h3','h4','h5','h6','h7','h8','h9','h10']
HALLWAY_LOCATIONS = ['h0','h1','h3','h5','h7','h9','h10']
ROOM_LOCATIONS = ['a0','a1','b0','b1','c0','c1','d0','d1']

AMPHIPODS ={
    "A0":{ "class":"a", "targetDestination":"a0", "parked":False, "cost":1},
    "A1":{ "class":"a", "targetDestination":"a0", "parked":False, "cost":1},
    "B0":{ "class":"b", "targetDestination":"b0", "parked":False, "cost":10},
    "B1":{ "class":"b", "targetDestination":"b0", "parked":False, "cost":10},
    "C0":{ "class":"c", "targetDestination":"c0", "parked":False, "cost":100},
    "C1":{ "class":"c", "targetDestination":"c0", "parked":False, "cost":100},
    "D0":{ "class":"d", "targetDestination":"d0", "parked":False, "cost":1000},
    "D1":{ "class":"d", "targetDestination":"d0", "parked":False, "cost":1000},
}

GRAPH = {
    'a0'  : {"occupiedBy":None, "connectedTo":["a1"]},
    'a1'  : {"occupiedBy":None, "connectedTo":["a0","h2"]},
    'b0'  : {"occupiedBy":None, "connectedTo":["b1"]},
    'b1'  : {"occupiedBy":None, "connectedTo":["b0","h4"]},
    'c0'  : {"occupiedBy":None, "connectedTo":["c1"]},
    'c1'  : {"occupiedBy":None, "connectedTo":["c0","h6"]},
    'd0'  : {"occupiedBy":None, "connectedTo":["d1"]},
    'd1'  : {"occupiedBy":None, "connectedTo":["d0","h8"]},
    'h0'  : {"occupiedBy":None, "connectedTo":["h1"]},
    'h1'  : {"occupiedBy":None, "connectedTo":["h0","h2"]},
    'h2'  : {"occupiedBy":None, "connectedTo":["h1","a1","h3"]},
    'h3'  : {"occupiedBy":None, "connectedTo":["h2","h4"]},
    'h4'  : {"occupiedBy":None, "connectedTo":["h3","b1","h5"]},
    'h5'  : {"occupiedBy":None, "connectedTo":["h4","h6"]},
    'h6'  : {"occupiedBy":None, "connectedTo":["h5","c1","h7"]},
    'h7'  : {"occupiedBy":None, "connectedTo":["h6","h8"]},
    'h8'  : {"occupiedBy":None, "connectedTo":["h7","d1","h9"]},
    'h9'  : {"occupiedBy":None, "connectedTo":["h8","h10"]},
    'h10' : {"occupiedBy":None, "connectedTo":["h9"]}
}

STACK = [{"type":"start", "totalCost":0, "parkedAmphipods":0}]

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed = []
    
    processed.append(raw[2].split('#')[3:7])
    processed.append(raw[3].split('#')[1:5])

    counters = {"A":-1,"B":-1,"C":-1,"D":-1}
    roomClasses = ['a','b','c','d']

    for j in range(1,-1,-1):
        for i in range(4):
            amphipodClass = processed[1-j][i]
            counters[amphipodClass]+=1
            amphipodName = "%s%d" % (amphipodClass, counters[amphipodClass])
            GRAPH["%s%d" % (roomClasses[i], j)]["occupiedBy"] = amphipodName 

def logGraph():
    def representOccupance(location):
        oBy = GRAPH[location]["occupiedBy"]
        return '.' if not oBy else (light(oBy[0]) if AMPHIPODS[oBy]["parked"]  else oBy[0])

    m = matrixUtils.generate(5,11,' ')

    for i in range(11):
        m[1][i] = representOccupance('h%d' % i) 

    m[2][2] = representOccupance("a1")
    m[3][2] = representOccupance("a0")
    m[2][4] = representOccupance("b1")
    m[3][4] = representOccupance("b0")
    m[2][6] = representOccupance("c1")
    m[3][6] = representOccupance("c0")
    m[2][8] = representOccupance("d1")
    m[3][8] = representOccupance("d0")

    # matrixUtils.log(m, '', log, lambda e: red(e) if e == 'A' else (green(e) if e =='B' else (blue(e) if e == 'C' else (purple(e) if e == 'D' else e))))

def findRoute(start, stop, route, checkObstructions=True):
    route.append(start)

    if start == stop:
        return route
    else:
        for connection in GRAPH[start]["connectedTo"]:
            if not connection in route and (not checkObstructions or GRAPH[connection]["occupiedBy"] == None):
                result = findRoute(connection, stop, []+route, checkObstructions)

                if result != None:
                    return result

        return None

def moveAmphipod(amphipodName, stop, meta):
    start = getAmphipodLocation(amphipodName)
    path = findRoute(start, stop, [])

    if path == None:
        return False
    else:
        GRAPH[start]["occupiedBy"] = None
        GRAPH[stop]["occupiedBy"] = amphipodName

        cost = AMPHIPODS[amphipodName]["cost"] * (len(path)-1)

        STACK.append({"type":"move", "meta":meta, "amphipod":amphipodName, "from":start, "to":stop, "totalCost":STACK[-1]["totalCost"] + cost, "parkedAmphipods":STACK[-1]["parkedAmphipods"]})

        return True

def countAndParkParkedAmphipods():
    parkedAmphipodsCount = 0

    # check for amphipods that are already parked
    for location in GRAPH:
        if GRAPH[location]["occupiedBy"]:
            amphipodName = GRAPH[location]["occupiedBy"]
            amphipod = AMPHIPODS[amphipodName]
            
            if not amphipod["parked"] and amphipod["targetDestination"] == location:
                # log(green("Found parked amphipod!", amphipodName, amphipod))
                amphipod["parked"] = True
                parkedAmphipodsCount+=1

                # change the desired target, once it was reached
                for otherAmphipodName in AMPHIPODS:
                    otherAmphipod = AMPHIPODS[otherAmphipodName]
                    if otherAmphipod["class"] == amphipod["class"] and not otherAmphipod["parked"]:
                        otherAmphipod["targetDestination"] = '%s1' % otherAmphipod["class"]

    return parkedAmphipodsCount

def getAmphipodLocation(amphipodName):
    for location in GRAPH:
        if GRAPH[location]["occupiedBy"] == amphipodName:
            return location

# GLOBALS={
#     "RP_COUNTER" : 0,
#     "RP_CHOICE_COUNTER" : 0
# }

def revertToPrevRestorePoint():
    while True:
        while (STACK[-1]["type"] == "move"):
            move = STACK[-1]
            # log(dark("undo", move))
            
            if move["meta"] == "parking":
                amphipod = AMPHIPODS[move["amphipod"]]
                amphipod["parked"] = False
                for otherAmphipod in [AMPHIPODS[a] for a in AMPHIPODS if AMPHIPODS[a]["class"] == amphipod["class"] and not AMPHIPODS[a]["parked"]]:
                    # otherAmphipod["targetDestination"] = '%s%d' % (otherAmphipod["class"], (int(getAmphipodLocation(move["amphipod"])[1])-1))
                    otherAmphipod["targetDestination"] = amphipod["targetDestination"]

            GRAPH[move["to"]]["occupiedBy"] = None
            GRAPH[move["from"]]["occupiedBy"] = move["amphipod"]
            
            del STACK[-1]

        previousRestorePoint = STACK[-1]
        if previousRestorePoint["type"] == 'restorePoint':
            previousRestorePoint["moveIndex"]+=1
            # GLOBALS["RP_CHOICE_COUNTER"]=previousRestorePoint["moveIndex"]

            if previousRestorePoint["moveIndex"]<len(previousRestorePoint["availableMoves"]):
                break
            else:
                # GLOBALS["RP_COUNTER"]-=1
                del STACK[-1]
        else:
            return False
            
    return True



def solution(inputFile):

    getInputData(inputFile)

    STACK[0]["parkedAmphipods"] = countAndParkParkedAmphipods()  

    minCost = -1
    noMoreRestorePoints = False
    bestStack = None

    while not noMoreRestorePoints:
        while STACK[-1]["parkedAmphipods"]<len(AMPHIPODS):
            # log(GLOBALS["RP_COUNTER"], GLOBALS["RP_CHOICE_COUNTER"])
            # log(AMPHIPODS)
            # time.sleep(0.2)

            # look for parking routes
            foundMove = False
            for amphipodName in [a for a in AMPHIPODS if not AMPHIPODS[a]["parked"]]:
                if moveAmphipod(amphipodName, AMPHIPODS[amphipodName]["targetDestination"], "parking"):
                    foundMove = True

                    # found parked amphipod!
                    amphipod = AMPHIPODS[amphipodName]

                    # log(green("Found parked amphipod!", amphipodName))
                    amphipod["parked"] = True

                    STACK[-1]["parkedAmphipods"]+=1

                    # change the desired target, for the rest amphipods with the same class
                    for otherAmphipod in [AMPHIPODS[a] for a in AMPHIPODS if AMPHIPODS[a]["class"] == amphipod["class"] and not AMPHIPODS[a]["parked"]]:
                        otherAmphipod["targetDestination"] = '%s%d' % (otherAmphipod["class"], int(amphipod['targetDestination'][1])+1)

            if not foundMove:
                # if no park routes found, search for available hallway moves
                restorePointMoves = []

                for amphipodName in [a for a in AMPHIPODS if not AMPHIPODS[a]["parked"]]:
                    amphipodLocation = getAmphipodLocation(amphipodName)
                    if not 'h' in amphipodLocation:
                        # amphipod is in room
                        possibleDestinations = [d for d in HALLWAY_LOCATIONS if findRoute(amphipodLocation, d, []) != None]
                        
                        if len(possibleDestinations) > 0:
                            for destination in possibleDestinations:
                                restorePointMoves.append((amphipodName, destination))
    
                if len(restorePointMoves) == 0:
                    # no available hallway moves -> deadend
                    # log(red("All amphipods blocked - bad guess... Will undo to previous restore point"))

                    if not revertToPrevRestorePoint():
                        # no more restore points
                        noMoreRestorePoints = True
                        break

                    newMove = STACK[-1]["availableMoves"][STACK[-1]["moveIndex"]]
                    moveAmphipod(newMove[0], newMove[1], 'try')
                else:
                    # create restore point with available moves
                    STACK.append({"type":"restorePoint", "moveIndex":0, "availableMoves":restorePointMoves, "totalCost":STACK[-1]["totalCost"], "parkedAmphipods":STACK[-1]["parkedAmphipods"]})
                    # GLOBALS["RP_COUNTER"]+=1
                    # GLOBALS["RP_CHOICE_COUNTER"]=0
                   
                    move = restorePointMoves[0]

                    # try the first move
                    moveAmphipod(move[0], move[1], 'try')

            if minCost>-1 and STACK[-1]["totalCost"]>minCost:
                noMoreRestorePoints = not revertToPrevRestorePoint()

                if not noMoreRestorePoints:
                    newMove = STACK[-1]["availableMoves"][STACK[-1]["moveIndex"]]
                    moveAmphipod(newMove[0], newMove[1], 'try')
                else:
                    break

        if noMoreRestorePoints:
            # log("No more restore points on stack...")
            break

        currentCost = STACK[-1]["totalCost"]
        if minCost == -1:
            # log(dark(STACK))
            minCost = currentCost
            # log('Greedy solution', currentCost)
        elif currentCost<minCost:
            # log(dark(STACK))
            # log(green('Better solution', currentCost))
            minCost = currentCost

            bestStack = []+STACK
        # else:
        #     log(red('Worse solution...', currentCost))

        if not revertToPrevRestorePoint():
            # log("No more restore points on stack...")
            break

        newMove = STACK[-1]["availableMoves"][STACK[-1]["moveIndex"]]
        moveAmphipod(newMove[0], newMove[1], 'try')

    # log(bestStack)
    result = minCost
    return (result,14371)

 
