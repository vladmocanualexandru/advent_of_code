import sys, os, math, re

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

MAX_EXPLOSIONS = 1
MAX_SPLITS = 1

class SFNumber:
    left=right=None


    def __init__(self, left, right):
        if '[' in left:
            self.left=SFNumber()
            
        self.right=right

def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    return raw


def solution(inputFile):

    # def logSFN(sFN):
    #     return ''.join(sFN)

    def add(sFN1, sFN2):
        return ['[']+sFN1 + [','] + sFN2 + [']']

    def resolveExplosion(sFN):
        newSFN = []
        
        bracketRatio = 0
        i=0
        explosionCount = 0
        while i<len(sFN):
            bracketRatio += 1 if sFN[i] == '[' else -1 if sFN[i]==']' else 0

            if bracketRatio==5 and explosionCount<MAX_EXPLOSIONS:
                skipValue = leftVal = rightVal = 0
                if sFN[i+4] == ']':
                    leftVal = int(sFN[i+1])
                    rightVal = int(sFN[i+3])
                    skipValue = 5
                elif sFN[i+5] == ']' and sFN[i+2] == ',':
                    leftVal = int(''.join(sFN[i+1:i+2]))
                    rightVal = int(''.join(sFN[i+3:i+5]))
                    skipValue = 6
                elif sFN[i+5] == ']' and sFN[i+3] == ',':
                    leftVal = int(''.join(sFN[i+1:i+3]))
                    rightVal = int(''.join(sFN[i+4:i+5]))
                    skipValue = 6
                else:
                    leftVal = int(''.join(sFN[i+1:i+3]))
                    rightVal = int(''.join(sFN[i+4:i+6]))
                    skipValue = 7

                # look in newSFN for the first number (2 digits max) and add left value
                for j in range(len(newSFN)-1, 1, -1):
                    if newSFN[j].isnumeric():
                        value = int(newSFN[j])

                        if newSFN[j-1].isnumeric():
                            value += int(newSFN[j-1])*10
                            newSFN.pop(j)
                            j-=1

                        newSFN.pop(j)
                        for d in list(str(value+leftVal)):
                            newSFN.insert(j, d)
                            j+=1
                        break

                newSFN = newSFN + ['0'] 
                i+=skipValue

                # look in sFN for the first number (2 digits max) and add right value
                for j in range(i, len(sFN)-1):
                    i+=1

                    if sFN[j].isnumeric():
                        value = int(sFN[j])

                        if sFN[j+1].isnumeric():
                            value = value*10+ int(sFN[j+1])
                            i+=1

                        newSFN = newSFN + list(str(value+rightVal))
                        break
                    else:
                        newSFN = newSFN + [sFN[j]] 

                explosionCount+=1
            else:
                newSFN = newSFN + sFN[i:i+1]
                i+=1


        return (explosionCount>0, newSFN)

    def resolveSplit(sFN):
        newSFN = []

        i=0
        splitCount = 0
        while i<len(sFN)-1:
            if sFN[i].isnumeric() and sFN[i+1].isnumeric() and splitCount<MAX_SPLITS:
                splitCount+=1
                
                value = int(sFN[i])*10+int(sFN[i+1])
                newSFN = newSFN + ['['] + list(str(math.floor(value/2))) + [','] + list(str(math.ceil(value/2))) + [']']


                i+=2
            else:
                newSFN = newSFN + [sFN[i]]
                i+=1

        newSFN=newSFN + [sFN[-1]]

        return (splitCount>0, newSFN)

    def calculateMagnitude(sFN):
        resultFound = False
        sFNStr = ''.join(sFN)

        while not resultFound:
            resultFound = True

            for pair in re.findall("\[(\d+,\d+)]", sFNStr):
                pairStr = '[%s]' % pair

                numbers = pair.split(',')

                sFNStr = sFNStr.replace(pairStr, str(int(numbers[0])*3+int(numbers[1])*2))
                resultFound = False
            
        return sFNStr

    inputData = getInputData(inputFile)

    result = inputData[0]

    for sFN in inputData[1:]:
        result = add(result, sFN)

        stable = False
        while not stable:
            stable = True

            explodeResult = resolveExplosion(result)
            if explodeResult[0]:
                result = explodeResult[1]
                stable = False

                continue
            
            splitResult = resolveSplit(result)
            if splitResult[0]:
                result = splitResult[1]
                stable = False

                continue


    # log(logSFN(result))

    return (int(calculateMagnitude(result)),4391)

 
