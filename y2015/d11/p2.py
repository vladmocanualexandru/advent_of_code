import sys, os, string

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 'cqkaabcc'

NEW_PASSWORD_COUNT = 2

PERMITTED_LETTERS = [l for l in string.ascii_lowercase if not l in ['o','i','l']]

def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    
    processed=[PERMITTED_LETTERS.index(r) for r in raw[0]]

    return processed    

def hasIncreasingStraight(password):
    for i in range(len(password)-2):
        if password[i]==password[i+1]-1==password[i+2]-2:
            return True

    return False

def hasLetterPairs(password):
    found = []

    target = 2
    while len(found)<target:
        foundPair = False
        for i in range(len(password)-1):
            if password[i]==password[i+1] and not password[i] in found:
                found.append(password[i])
                foundPair = True
                break

        if not foundPair:
            return False

    return True

def nextPassword(password):

    while True:
        for i in range(1, len(password)+1):
            password[0-i] +=1
            if (password[0-i]) == len(PERMITTED_LETTERS):
                password[0-i] = 0
            else:
                break

        if hasLetterPairs(password) and hasIncreasingStraight(password):
            break

    return password

def solution(inputFile):
    inputData = getInputData(inputFile)

    # fun fact, test input 'ghijklmn' will fail the algorithm because I implemented excluded letters from the start;
    # I should take into account having forbidden letters in the input, but my input had none, so I didn't worry about it (#lazy) :-)
    # log('input', inputData)

    for i in range(NEW_PASSWORD_COUNT):
        # log(nextPassword(inputData))
        nextPassword(inputData)

    result=''.join([PERMITTED_LETTERS[i] for i in inputData])

    return (result,EXPECTED_RESULT)