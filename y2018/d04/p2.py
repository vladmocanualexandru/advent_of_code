import sys, os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *

EXPECTED_RESULT = 12725

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
    
    if len(shift["events"])==0:
        return False

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
            shift = {"guard_id": int(logEntry[1].replace(' begins shift', '')[7:]), "events":[], "day": logEntry[0].day, "month": logEntry[0].month}

            # if logEntry[0].hour == 23:
            #     shift["day"]+=1
        else:
            shift["events"].append(logEntry)

    # handle last shift 
    shift["sleeping_minutes"] = calculateSleepingMinutes(shift)
    shifts.append(shift) 

    # log(shifts)



    # find minute that each guard was most asleep
    minuteCounts = {}

    for shift in shifts:
        if not shift['guard_id'] in minuteCounts:
            minuteCounts[shift['guard_id']] = [0 for m in range(60)]

        for minute in range(60):
            if checkSleepingMinute(minute, shift):
                minuteCounts[shift['guard_id']][minute]+=1

    # map minutes to counts so that they can be sorted
    minuteCountMap = {}

    for guard in minuteCounts:
        temp = [(i, minuteCounts[guard][i]) for i in range(60)]
        temp.sort(key=lambda e : e[1], reverse=True)

        minuteCountMap[guard] = temp[0]

    #flatten minuteCountMap
    flatMinuteCountMap = [(guard, minuteCountMap[guard][0], minuteCountMap[guard][1]) for guard in minuteCountMap]
    flatMinuteCountMap.sort(key=lambda e: e[2], reverse=True)

    result = flatMinuteCountMap[0][0]*flatMinuteCountMap[0][1]

    # visualization of the sleeping guards
    # log('Date   ID     Minute')
    # log('              000000000011111111112222222222333333333344444444445555555555')
    # log('              012345678901234567890123456789012345678901234567890123456789')

    # for shift in shifts:
    #     shiftRep = []
    #     for minute in range(60):
    #         if checkSleepingMinute(minute, shift):
    #             shiftRep.append(light('Z'))
    #         else:
    #             shiftRep.append(C_HORIZ_LINE)
                
    #     log('%02d-%02d  #%04d  %s' % (shift["month"], shift["day"], shift["guard_id"], ''.join(shiftRep)))

    return (result,EXPECTED_RESULT)

 
