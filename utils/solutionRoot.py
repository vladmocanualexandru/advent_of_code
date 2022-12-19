import time

# from utils.terminalUtils import *
# from utils.labelMakerUtils import *
# from utils import *

import utils as utils

startMs = round(time.time()*1000)

def log(*output):
    msDiff = round(time.time()*1000 - startMs)
    print('%s %s' % (utils.terminalUtils.dark(utils.labelMakerUtils.formatElapsedMsConsole(msDiff)), ' '.join(str(e) for e in output)))

def logMatrix(matrix, logFunc=log, separator='', highlightElem=(lambda e: str(e))):
    return utils.matrixUtils.log(matrix, logFunc, separator, highlightElem)

def runSolution(solutionLogic, inputFile="input.txt"):
    log(utils.terminalUtils.light('---------------------------------------- START -----------------------------------------'))

    result = solutionLogic(inputFile)
    log(utils.terminalUtils.yellow('RESULT',result))

    log(utils.terminalUtils.dark('---------------------------------------- STOP ------------------------------------------'))




