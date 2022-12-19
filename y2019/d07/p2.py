import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))
sys.path.append(os.path.abspath(os.path.join('..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

import y2019.int_code_computer as int_code_computer
 
EXPECTED_RESULT = 58285150

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,',')
    
    processed=raw[0]

    return processed 

def computeSequence(sequence, program):
    amps = [{"mem":int_code_computer.initializeMemory([]+program), "status":""} for i in range(5)]

    mem = amps[0]["mem"]
    mem["input"]=[sequence[0],0]
    ampOutput = int_code_computer.run(mem, 0)

    mem = amps[1]["mem"]
    mem["input"]=[sequence[1],ampOutput[1][0]]
    ampOutput = int_code_computer.run(mem, 0)

    mem = amps[2]["mem"]
    mem["input"]=[sequence[2],ampOutput[1][0]]
    ampOutput = int_code_computer.run(mem, 0)

    mem = amps[3]["mem"]
    mem["input"]=[sequence[3],ampOutput[1][0]]
    ampOutput = int_code_computer.run(mem, 0)

    mem = amps[4]["mem"]
    mem["input"]=[sequence[4],ampOutput[1][0]]
    ampOutput = int_code_computer.run(mem, 0)

    while True:
        for i in range(5):
            signalValue = ampOutput[1][0]

            amp = amps[i]

            amp["mem"]["input"] = [signalValue]
            ampOutput = int_code_computer.run(amp["mem"], 0)

            amp["status"] = ampOutput[0]

        if amps[-1]["status"] == 'OK':
            signalValue = ampOutput[1][0]
            break
    
    return signalValue
  

def sequenceIsUnique(sequence):
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            if sequence[i] == sequence[j]:
                return False
    return True

def solution(inputFile):
    program = getInputData(inputFile)

    sequence = [5,6,7,8,9]

    result = -1
    resultFound = False
    while not resultFound:
        if sequenceIsUnique(sequence):
            localResult = computeSequence(sequence, program)
            # log(blue('Sequence %s -> signal %d' % (str(sequence), localResult)))

            result = max(result, localResult)

        sequence[-1]+=1
        for i in range(len(sequence)-1,-1,-1):
            if sequence[i]==10:
                if i==0:
                    # final sequence has been generated; result contains the maximum signal
                    resultFound = True
                    break

                sequence[i]=5
                sequence[i-1]+=1

    return (result,EXPECTED_RESULT)

 
