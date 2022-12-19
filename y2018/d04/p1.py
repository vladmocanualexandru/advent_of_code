import sys, os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 
EXPECTED_RESULT = 119835

def getInputData(inputFile):
    raw = getTuples_text(inputFile,'] ')

    processed=[[datetime.strptime(r[0][1:], '%Y-%m-%d %H:%M'), r[1]] for r in raw]

    processed.sort(key = lambda e: (e[0]))

    return processed 

def calculateSleepingMinutes(shift):
    result = 0

    start = None
    for event in shift["events"]:
        if event[1]=='falls asleep':
            start = event[0]
        else:
            delta = event[0] - start
            result += delta.total_seconds()/60

    return result

def checkSleepingMinute(minute, shift):
    minuteTS = datetime.strptime('1518-%d-%d 00:%d' % (shift["events"][0][0].month, shift["events"][0][0].day, minute), '%Y-%m-%d %H:%M')

    for eventIndex in range(len(shift["events"])):
        currentEvent = shift["events"][eventIndex]
        if currentEvent[1] == 'falls asleep' and minuteTS>=currentEvent[0] and minuteTS<shift["events"][eventIndex+1][0]:
            return True

    return False

def solution(inputFile):
    inputData = getInputData(inputFile)
    # matrixUtils.log(inputData[:20], ', ', log)

    shifts = []
    shift = {}

    for logEntry in inputData:
        if "Guard" in logEntry[1]:
            if not shift == {}:
                shift["sleeping_minutes"] = calculateSleepingMinutes(shift)
                shifts.append(shift) 

            # new shift
            shift = {"guard_id": int(logEntry[1].replace(' begins shift', '')[7:]), "events":[]}
        else:
            shift["events"].append(logEntry)

    # handle last shift 
    shift["sleeping_minutes"] = calculateSleepingMinutes(shift)
    shifts.append(shift) 

    # log(shifts)

    # (first half of the result) find guard with longest total sleep time
    guardSleepTimes = {}
    for shift in shifts:
        if not shift["guard_id"] in guardSleepTimes:
            guardSleepTimes[shift["guard_id"]] = shift["sleeping_minutes"]
        else:
            guardSleepTimes[shift["guard_id"]] += shift["sleeping_minutes"]

    resultFirstHalf = [(g, guardSleepTimes[g]) for g in guardSleepTimes]
    resultFirstHalf.sort(key=lambda e : e[1])
    sleepiestGuard = resultFirstHalf[-1][0]

    # (second half of the result) find minute that the guard was most asleep
    minuteCounts = [0 for m in range(60)]
    for shift in shifts:
        if shift['guard_id']==sleepiestGuard:
            for minute in range(60):
                if checkSleepingMinute(minute, shift):
                    minuteCounts[minute]+=1

    minuteCountMap = [(i, minuteCounts[i]) for i in range(60)]
    minuteCountMap.sort(key=lambda e : e[1], reverse=True)
    sleepiestMinute = minuteCountMap[0][0]

    result = sleepiestGuard*sleepiestMinute

    return (result,EXPECTED_RESULT)

 
