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
 
def getInputData(inputFile):
    raw = getNumbers_dec(inputFile)
    
    processed=[entry for entry in raw]

    return processed 

def solution(inputFile):
    numbers = getInputData(inputFile)

    # numbers2 = numbers+[]
    # numbers2.sort()
    # log(numbers2)

    # exit(1)

    for number in ([]+numbers):
        # log(numbers)
        currentPos = numbers.index(number)
        del numbers[currentPos]

        oldLeft = (currentPos-1)%len(numbers)
        oldRight = currentPos

        newLeft = (oldLeft+number)%len(numbers)
        newRight = (oldRight+number)%len(numbers)

        # log(number, "was between", oldLeft, oldRight)
        # log("will move to", newLeft, newRight)

        if newRight>newLeft:
            numbers = numbers[:newLeft+1]+[number]+numbers[newRight:]
        else:
            numbers = numbers + [number]


    # log(numbers)
    log(len(numbers))

    index0 = numbers.index(0)

    n1000 = numbers[(index0+1000)%len(numbers)]
    n2000 = numbers[(index0+2000)%len(numbers)]
    n3000 = numbers[(index0+3000)%len(numbers)]

    log(n1000,n2000,n3000)

    log(red(13642))

    return n1000+n2000+n3000