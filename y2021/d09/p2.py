import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

# def printCoveredArea():
#     for line in coveredArea:
#         outputLine = ''
#         for c in line:
#             if c == -2:
#                 outputLine = outputLine +  colorOutput_blue('█')
#             elif c==-1:
#                 outputLine = outputLine +  colorOutput_red('█')
#             else: 
#                 avg = statistics.mean(line)
                
#                 if c<avg:
#                     outputLine = outputLine +  colorOutput_yellow('█')
#                 else:
#                     outputLine = outputLine +  colorOutput_green('█')

#         print(outputLine)

# def printCoveredArea2():
#     for line in coveredArea:
#         outputLine = ''
#         for c in line:
#             if c == -2:
#                 outputLine = outputLine +  reverseColor('█')
#             elif c<0:
#                 outputLine = outputLine +  reverseColor(formatOutput(-c, 'X'))
#             else:
#                 outputLine = outputLine + formatOutput(c, '█')

#         log(outputLine)

def countBasinSize(lineIndex,colIndex, basinCode,coveredArea, input):
    if lineIndex<0 or colIndex<0 or lineIndex==len(input) or colIndex==len(input[0]) or input[lineIndex][colIndex]==9 or coveredArea[lineIndex][colIndex]>-2:
        return 0

    coveredArea[lineIndex][colIndex]=basinCode

    return sum([1, 
        countBasinSize(lineIndex-1,colIndex,basinCode,coveredArea,input),
        countBasinSize(lineIndex+1,colIndex,basinCode,coveredArea,input),
        countBasinSize(lineIndex,colIndex-1,basinCode,coveredArea,input),
        countBasinSize(lineIndex,colIndex+1,basinCode,coveredArea,input) ])

def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    processed = []

    for line in raw:
        processed.append([int(c) for c in line])

    return processed 

def solution(inputFile):

    input = getInputData(inputFile)


    input = getInputData(inputFile)

    coveredArea = [[-2 for c1 in range(len(input[0]))] for c2 in range(len(input))]

    result = 0

    lowPoints = []
    for lineIndex in range(len(input)):
        for colIndex in range(len(input[lineIndex])):
            value = input[lineIndex][colIndex]

            minNeighValue = 10
            if lineIndex>0:
                minNeighValue = min(minNeighValue,input[lineIndex-1][colIndex])
            if colIndex>0:
                minNeighValue = min(minNeighValue,input[lineIndex][colIndex-1])
            if lineIndex<len(input)-1:
                minNeighValue = min(minNeighValue,input[lineIndex+1][colIndex])
            if colIndex<len(input[lineIndex])-1:
                minNeighValue = min(minNeighValue,input[lineIndex][colIndex+1])
            
            if value < minNeighValue:
                lowPoints.append((lineIndex, colIndex))

    basinSizes = []

    availableColorCodes = [1,31,32,33,34,35,36,90]
    colorI=0
    for lowPoint in lowPoints:
        basinSizes.append(countBasinSize(lowPoint[0],lowPoint[1], availableColorCodes[colorI],coveredArea,input))

        colorI = (colorI+1)%len(availableColorCodes)
        coveredArea[lowPoint[0]][lowPoint[1]] = -1*coveredArea[lowPoint[0]][lowPoint[1]]
        
    basinSizes.sort()

    result = basinSizes[-1]*basinSizes[-2]*basinSizes[-3]

    return (result, 882942)