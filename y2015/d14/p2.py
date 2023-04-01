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

EXPECTED_RESULT = 1256

RACE_TIME_S=2503
 
def getInputData(inputFile):
	# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.

    raw = getTuples_text(inputFile, " can fly "," km/s for "," seconds, but then must rest for "," seconds.")
    
    processed=pd.DataFrame([(entry[0], int(entry[1]), int(entry[2]), int(entry[3])) for entry in raw], columns=["reindeer","speed_kms","flight_length_s","rest_s"]).set_index("reindeer")

    return processed 

def adjustStateChangeEtaS(e):
    if e["state_change_eta_s"] > 0:
        return e["state_change_eta_s"]
    
    if e["flying"]:
        return e["flight_length_s"]
    else:
        return e["rest_s"]

def solution(inputFile):
    rDeers = getInputData(inputFile)

    rDeers["flying"] = True
    rDeers["state_change_eta_s"] = rDeers["flight_length_s"]
    rDeers["total_km"] = 0
    rDeers["points"] = 0

    for second in range(RACE_TIME_S):
        rDeers["state_change_eta_s"] -= 1
        rDeers["total_km"] = rDeers.apply(lambda e: e["total_km"] + (e["speed_kms"] if e["flying"] else 0), axis=1)
        rDeers["flying"] = rDeers.apply(lambda e: not e["flying"] if e["state_change_eta_s"] == 0 else e["flying"], axis=1)
        rDeers["state_change_eta_s"] = rDeers.apply(adjustStateChangeEtaS, axis=1)

        topKm = np.max(rDeers["total_km"])

        rDeers["points"] = rDeers.apply(lambda e:e["points"]+(1 if e["total_km"] == topKm else 0), axis=1)

    result = np.max(rDeers["points"])

    return (result, EXPECTED_RESULT)