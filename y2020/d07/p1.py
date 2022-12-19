import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 142

def cleanBag(bag):
    return bag[2:].replace(' bags.', '').replace(' bags', '').replace(' bag.', '').replace(' bag', '').replace(' other', '')

def getInputData(inputFile):
    raw = getTuples_text(inputFile,' bags contain ')
    
    processed1=[]

    for line in raw:
        processed1.append((line[0], [cleanBag(c) for c in line[1].split(', ')]))

    processed2 = {}
    for entry in processed1:
        processed2[entry[0]] = entry[1]

    return processed2 

def searchForBags(criteria, allBags, resultBags):
    for bag in allBags:
        if criteria in allBags[bag]:
            resultBags[bag] = True
            searchForBags(bag, allBags, resultBags)

def solution(inputFile):
    inputData = getInputData(inputFile)
    # log(inputData)

    foundBags = {}

    searchForBags('shiny gold', inputData, foundBags)

    result=len(foundBags)

    return (result, EXPECTED_RESULT)

 
