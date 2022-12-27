import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

MINUTES_LIMIT = 24

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ": Each ore robot costs ", " ore. Each clay robot costs ", " ore. Each obsidian robot costs ", " ore and ", " clay. Each geode robot costs ", " ore and ", " obsidian.")
    
    processed=[{"Or":{"Or":int(entry[1])},"C":{"Or":int(entry[2])},"Ob":{"Or":int(entry[3]),"C":int(entry[4])},"G":{"Or":int(entry[5]),"Ob":int(entry[6])}} for entry in raw]

    return processed 

def analyzeMinute(minute, stock, robots, blueprint, solutionBin):

    if minute == MINUTES_LIMIT:
        solutionBin.append(stock)
        # log(green("stock", stock, "robots", robots))
        return stock

    for type in robots:
        stock[type] += robots[type]

    stockClone = stock.copy()
    robotsClone = robots.copy()

    # option 0: build nothing
    analyzeMinute(minute+1, stockClone, robotsClone, blueprint,solutionBin)

    # option 1-2-3-4...: build something
    for plan in blueprint:
        stockClone = stock.copy()
        robotsClone = robots.copy()

        for component in blueprint[plan]:
            stockClone[component]-=blueprint[plan][component]
            if stockClone[component]<0:
                break
        else:
            robotsClone[plan]+=1
            analyzeMinute(minute+1, stockClone, robotsClone, blueprint,solutionBin)

def solution(inputFile):
    blueprints = getInputData(inputFile)

    blueprint = blueprints[0]

    log(blue(blueprint))

    stock = {"Or":0, "C":0, "Ob":0, "G":0}
    robots = {"Or":1, "C":0, "Ob":0, "G":0}

    solutionBin = []
    analyzeMinute(0,stock,robots,blueprint, solutionBin)

    log(len(solutionBin))

    return None