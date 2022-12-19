import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 2016

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,'')[0]
    
    layers=[]

    lineCounter = 0
    layer = []
    for pos in range(0, len(raw), IMAGE_WIDTH):
        if lineCounter == IMAGE_HEIGHT:
            layers.append(layer)
            layer = []
            lineCounter = 0
        
        layer.append(raw[pos:pos+IMAGE_WIDTH])
        lineCounter+=1
    
    # don't forget about the final layer ;-)
    layers.append(layer)

    return layers 


def solution(inputFile):
    layers = getInputData(inputFile)

    targetLayerIndex = -1
    targetLayer0Count = IMAGE_WIDTH*IMAGE_HEIGHT

    for i in range(len(layers)):
        count0s = matrixUtils.addAll(layers[i], lambda e: e == 0, lambda e: 1)
        if count0s < targetLayer0Count:
            targetLayer0Count = count0s
            targetLayerIndex = i

        
    result = matrixUtils.addAll(layers[targetLayerIndex], lambda e: e == 1, lambda e: 1)
    result *= matrixUtils.addAll(layers[targetLayerIndex], lambda e: e == 2, lambda e: 1)

    return (result,EXPECTED_RESULT)

 

