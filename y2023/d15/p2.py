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

EXPECTED_RESULT = 230462
BOXES = 256

def getInputData(inputFile):
    raw = getTuples_text(inputFile,",")
    
    return raw[0] 

def explainStep(step):
    explanation = {"op":"remove", "box":0}

    if '=' in step:
        explanation["op"] = "add"
        explanation["focal"] = int(step[-1])
        step = step[:-2]
    else:
        step = step[:-1]

    explanation["label"] = step

    for c in step:
        explanation["box"]=(explanation["box"]+ord(c))*17%256

    return explanation 

def solution(inputFile):
    result = 0

    orderValue = 0
    boxes = [{} for i in range(BOXES)]
    
    steps = getInputData(inputFile)

    for step in steps:
        lens = explainStep(step)
        box = boxes[lens["box"]]

        if lens["op"] == 'remove':
            if lens["label"] in box:
                del box[lens["label"]]
        else:
            if lens["label"] in box:
                box[lens["label"]]["focal"] = lens["focal"]
            else:
                box[lens["label"]] = {"focal":lens["focal"], "order":orderValue}
                orderValue+=1

    for boxIndex in range(BOXES):
        box = boxes[boxIndex]
        lensCounter = 1
        for label in box:
            result += (boxIndex+1)*lensCounter*box[label]["focal"]
            # log(boxIndex, box[label])
            lensCounter+=1
    
    # log(boxes)    
    # log(red())
    return (result, EXPECTED_RESULT)