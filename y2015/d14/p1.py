import sys, os, math
import numpy as np
import pandas as pd
import math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = 2660

RACE_TIME_S=2503
 
def getInputData(inputFile):
	# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.

    raw = getTuples_text(inputFile, " can fly "," km/s for "," seconds, but then must rest for "," seconds.")
    
    processed=pd.DataFrame([(entry[0], int(entry[1]), int(entry[2]), int(entry[3])) for entry in raw], columns=["reindeer","speed_kms","flight_length_s","rest_s"]).set_index("reindeer")

    return processed 

def solution(inputFile):
    inputData = getInputData(inputFile)

    inputData["hop_distance_km"] = inputData["speed_kms"]*inputData["flight_length_s"]
    inputData["hop_duration_s"] = inputData["flight_length_s"] + inputData["rest_s"]
    inputData["hops"] = inputData["hop_duration_s"].apply(lambda e : math.floor(RACE_TIME_S/e))
    inputData["remaining_s"] = inputData["hop_duration_s"].apply(lambda e : math.floor(RACE_TIME_S%e))

    
    inputData["last_leg_km"] = inputData.apply(lambda e : min(e["flight_length_s"], e["remaining_s"]) * e["speed_kms"], axis=1)
    

    inputData["total_km"] = inputData["hops"] * inputData["hop_distance_km"] + inputData["last_leg_km"]
    
    result = np.max(inputData["total_km"])

    return (result, EXPECTED_RESULT)