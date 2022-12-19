import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def orderCharacters(string):
    chars =[c for c in string]
    chars.sort()
    return ''.join(chars)

def union(strings):
    result = [c for c in strings[0]]
    for s in strings[1:]:
        for c in s:
            if not c in result:
                result.append(c)

    result.sort()
    return ''.join(result)

def intersect(strings):

    result = []

    for c in strings[0]:
        found=True
        for s in strings[1:]:
            if not c in s:
                found=False
                break
        if found:
            result.append(c)

    result.sort()
    return ''.join(result)

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' | ')
    
    processed = [(entry[0].split(' '),entry[1].split(' ')) for entry in raw]

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)
    # input = [['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab','cdfeb fcadb cdfeb cdbaf']]

    # input = [(entry[0].split(' '),entry[1].split(' ')) for entry in input]

    result = 0
    for entry in input:
        digitsMap = ['' for i in range(10)]

        clues = [orderCharacters(clue) for clue in entry[0]]
        solution = [orderCharacters(solution) for solution in entry[1]]
        
        clues.sort(key = lambda x: (len(x)))

        digitsMap[1] = clues[0]
        digitsMap[4] = clues[2]
        digitsMap[7] = clues[1]
        digitsMap[8] = clues[9]

        for i in range(6,9):
            if intersect([clues[i], digitsMap[4]])==digitsMap[4]:
                digitsMap[9] = clues[i]
                break

        # log(digitsMap[9])

        # digitsMap[9] = [u for u in [
        #     union([digitsMap[4], clues[3], clues[4]]),
        #     union([digitsMap[4], clues[4], clues[5]]),
        #     union([digitsMap[4], clues[3], clues[5]])] 
        #         if len(u)==6][0]
        # log(digitsMap[9])

        for i in range(3,6):
            if len(intersect([digitsMap[9], clues[i]]))==4:
                digitsMap[2] = clues[i]
            elif union([clues[i], digitsMap[1]])==clues[i]:
                digitsMap[3] = clues[i]
            else:
                digitsMap[5] = clues[i]

        for i in range(6,9):
            if clues[i]!=digitsMap[9]:
                if union([clues[i],digitsMap[5]])==clues[i]:
                    digitsMap[6] = clues[i]
                else:
                    digitsMap[0] = clues[i]


        decryptedSolution = ''
        for digit in solution:
            if digit in digitsMap:
                decryptedSolution = decryptedSolution+str(digitsMap.index(digit))
            else:
                decryptedSolution = decryptedSolution+'_'
        
        # log(decryptedSolution)

        result += int(decryptedSolution)

    return (result,1019355)