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

EXPECTED_RESULT = 125742456
 
def getInputData(inputFile):
    raw = getStrings(inputFile)

    seeds = [int(e) for e in raw[0].split(' ')[1:]]
    
    processed=raw[1:]

    return (seeds, processed)

def convert(val, converter):
    for rule in converter:
        if val>=rule["min"] and val <= rule["max"]:
            return rule["dest"] + val-rule["min"]

    return val

seed2Soil = []
soil2Fertilizer = []
fertilizer2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []

def convertFull(seed):
    seed = convert(seed, seed2Soil)
    seed = convert(seed, soil2Fertilizer)
    seed = convert(seed, fertilizer2water)
    seed = convert(seed, water2light)
    seed = convert(seed, light2temperature)
    seed = convert(seed, temperature2humidity)
    seed = convert(seed, humidity2location)

    return seed

def solution(inputFile):
    result = pow(10,20)

    (seeds, mappings) = getInputData(inputFile)

    flow = [seed2Soil, soil2Fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location]
    
    flowIndex = -1
    for mapping in mappings:
        if mapping == '':
            continue
        if not mapping[0].isdigit():
            flowIndex+=1
            continue
        [destMin, srcMin, size] = [int(e) for e in mapping.split(' ')]
        
        flow[flowIndex].append({"min": srcMin, "max":srcMin+size-1, "dest":destMin})

    for seedIndex in range(0,len(seeds), 2): 
        seedStart = seeds[seedIndex]
        seedStop = seedStart + seeds[seedIndex+1] - 1

        step = 1000000
        while step>=1:
            oldSeed = convertFull(seedStart)
            if oldSeed<result:
                result = oldSeed
                step/=10
                continue

            for seed in range(seedStart+1, seedStop, int(step)):
                newSeed = convertFull(seed)
                if newSeed<result:
                    result = newSeed
                    seedStop = seed
                    seedStart = oldSeed
                    step/=10
                    break
                else:
                    oldSeed=seed
            else:
                break



        # log(seed, newSeed)

        # result = min(result, seed)

    # log(seed2Soil)
    # log(soil2Fertilizer)
    # log(fertilizer2water)
    # log(water2light)
    # log(light2temperature)
    # log(temperature2humidity)
    # log(humidity2location)

    # log(convert(79, seed2Soil))


    return (result, EXPECTED_RESULT)