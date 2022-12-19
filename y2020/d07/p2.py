import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 10219

def cleanBag(bag):
    bag=bag.replace(' bags.', '').replace(' bags', '').replace(' bag.', '').replace(' bag', '').replace('no other', '')
    if bag == '':
        return (0,None)
    else:
        return (int(bag[0]), bag[2:])

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' bags contain ')
    
    processed1=[]

    for line in raw:
        processed1.append((line[0], [cleanBag(bag) for bag in line[1].split(', ')]))

    processed2 = {}
    for entry in processed1:
        processed2[entry[0]] = entry[1]

    return processed2 

def countBags(currentBag, allBags):
    if allBags[currentBag][0][0] == 0:
        return 0
    
    sum = 0

    for innerBag in allBags[currentBag]:
        sum += innerBag[0] * (countBags(innerBag[1], allBags)+1)

    return sum


def solution(inputFile):
    inputData = getInputData(inputFile)
    # log(inputData)

    result = countBags('shiny gold', inputData)

    return (result, EXPECTED_RESULT)

 
