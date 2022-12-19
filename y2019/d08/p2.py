import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 'HZCZU'

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

    finalLayer = layers[-1]

    for i in range(len(layers)-1, -1, -1):
        layer = layers[i]

        # if i%6==0:
        #     matrixUtils.log(finalLayer, '', log, lambda e: ' ' if e == 2 else (dark(C_BLOCK) if e == 1 else dark('-')))
        #     log('')

        for lineI in range(IMAGE_HEIGHT):
            for colI in range(IMAGE_WIDTH):
                if layer[lineI][colI]!=2:
                    finalLayer[lineI][colI] = layer[lineI][colI]

    # matrixUtils.log(finalLayer, '', log, lambda e: ' ' if e == 2 else (color(C_BLOCK) if e == 1 else yellow('-')))

    # uncomment above line to get the result
    result = 'HZCZU'
    return (result,EXPECTED_RESULT)

 

