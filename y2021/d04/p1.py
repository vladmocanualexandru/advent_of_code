import sys, os, math

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def boardHasBingo(board):
    for i in range(5):
        if sum(board[i])==0 or (board[0][i]+board[1][i]+board[2][i]+board[3][i]+board[4][i])==0:
            return True

def calculateBoardSum(board):
    return sum(board[0])+sum(board[1])+sum(board[2])+sum(board[3])+sum(board[4])

def calculateBoardDifference(board):
    result = 0
    for line in board:
        for number in line:
            if number>0:
                result+=1

    return result

def markNumberOnBoard(board, number):
    for line in board:
        for col in range(5):
            if line[col] == number:
                line[col] = 0

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ',')
    
    processed=[r for r in raw]

    return processed 

def solution(inputFile):
    rawInput = getInputData(inputFile)

    bingoNumbers = [(int(numeric_string)+1) for numeric_string in rawInput[0]]
    boards = []

    rawInput.pop(0)
    rawInput.pop(0)

    board = []
    for line in rawInput:
        if line==['']:
            boards.append(board)
            board = []
        else:
            board.append([(int(numeric_string)+1) for numeric_string in line[0].replace('  ', ' ').split(' ')])

    boards.append(board)

    result = 0

    bingoCalled = False
    for bingoNumber in bingoNumbers:
        for board in boards:
            markNumberOnBoard(board, bingoNumber)

            if boardHasBingo(board):
                # log("BINGO! Number %s, board %s" % (bingoNumber, board))
                bingoCalled = True

                result = (calculateBoardSum(board)-calculateBoardDifference(board))*(bingoNumber-1)

                break
        
        if bingoCalled:
            break

    return (result, 45031)