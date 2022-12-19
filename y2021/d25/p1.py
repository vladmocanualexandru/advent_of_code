import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_text(inputFile, '')
    return raw


def solution(inputFile):
    matrix = getInputData(inputFile)

    # matrixUtils.log(inputData,'',log)

    HEIGHT = len(matrix)
    WIDTH = len(matrix[0])
    
    steps = 0
    stillMoving = True

    while(stillMoving):
        stillMoving = False

        newMatrix = matrixUtils.generate(HEIGHT, WIDTH, 'x')
        for y in range(HEIGHT):
            x = 0
            while x<WIDTH:
                if matrix[y][x] == '>':
                    nextPosition = (y,(x+1)%WIDTH)

                    if matrix[nextPosition[0]][nextPosition[1]] == '.':
                        # log(y,x)
                        # matrixUtils.log(inputData,' ',log, lambda e: yellow(e) if e=='>' else dark(e))
                        # input("")
            
                        stillMoving = True
                        newMatrix[nextPosition[0]][nextPosition[1]] = '>'
                        newMatrix[y][x] = '.'

                x+=1

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if newMatrix[y][x] != 'x':
                    matrix[y][x] = newMatrix[y][x] 
        
        newMatrix = matrixUtils.generate(HEIGHT, WIDTH, 'x')
        for x in range(WIDTH):
            y = 0
            while y<HEIGHT:
                if matrix[y][x] == 'v':
                    # log('found', y, x)
                    nextPosition = ((y+1)%HEIGHT,x)
                    # log('next', nextPosition)
                    # matrixUtils.log(inputData,'',log)


                    if matrix[nextPosition[0]][nextPosition[1]] == '.':
                        # log(y,x)
                        # matrixUtils.log(matrix,' ',log, lambda e: yellow(e) if e=='v' else dark(e))
                        # input("")

                        stillMoving = True
                        newMatrix[nextPosition[0]][nextPosition[1]] = 'v'
                        newMatrix[y][x] = '.'

                y+=1

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if newMatrix[y][x] != 'x':
                    matrix[y][x] = newMatrix[y][x] 

        steps+=1
        # log(steps)

        # matrixUtils.log(matrix,'',log)
        # input("")

    # matrixUtils.log(matrix,'',log)

    return (steps,579)

 
