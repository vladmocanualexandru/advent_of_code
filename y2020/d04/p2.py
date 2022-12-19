import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 103

def validatePassportFieldValues(passport):
    # 'byr': '1937', 
    try:
        field_value = int(passport['byr'])

        if field_value<1920 or field_value>2002:
            # outside permitted range
            return False
    except ValueError:
        # not a proper number
        return False

    # 'iyr': '2017', 
    try:
        field_value = int(passport['iyr'])

        if field_value<2010 or field_value>2020:
            # outside permitted range
            return False
    except ValueError:
        # not a proper number
        return False

    # 'eyr': '2020', 
    try:
        field_value = int(passport['eyr'])

        if field_value<2020 or field_value>2030:
            # outside permitted range
            return False
    except ValueError:
        # not a proper number
        return False
    
    # 'hgt': '183cm', 
    try:
        field_value = int(passport['hgt'][:len(passport['hgt'])-2])

        minValue = maxValue = 0
        if 'cm' in passport['hgt']:
            minValue = 150
            maxValue = 193
        elif 'in' in passport['hgt']:
            minValue = 59
            maxValue = 76
        else:
            return False

        if field_value<minValue or field_value>maxValue:
            # outside permitted range
            return False
    except ValueError:
        # not a proper number
        return False

    # 'hcl': '#fffffd', 
    try:
        field_value = passport['hcl']

        if not field_value[0] == '#' or not len(field_value)==7:
            # wrong format
            return False
        else:
            int('0x'+field_value[1:], 16)
    except ValueError:
        # not a proper number
        return False

    # 'ecl': 'gry',
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # 'pid': '860033327', 
    try:
        field_value = passport['pid']

        if not len(field_value) == 9:
            return False

        int(field_value)
    except ValueError:
        # not a proper number
        return False

    # all checks passed!
    return True

def generatePassport(passportInfo):
    passport = {'fieldCount':0}
    for line in passportInfo:
        for t in line.split(' '):
            info = t.split(':')
            if info[0] == 'cid':
                continue

            passport[info[0]] = info[1]
            passport['fieldCount'] += 1 

    passport['fieldCountValid'] = passport['fieldCount']==7

    return passport

def getInputData(inputFile):
    raw = getStrings(inputFile)

    processed=[]
    passportInfo = []

    for line in raw:
        if not line == '':
            passportInfo.append(line)
        else:
            # passport info collected
            processed.append(generatePassport(passportInfo))
            passportInfo = []

    # process last passport
    processed.append(generatePassport(passportInfo))

    return processed 



def solution(inputFile):
    inputData = getInputData(inputFile)
    # log('sample', inputData[0])

    result=0

    for passport in inputData:
        if passport['fieldCountValid'] and validatePassportFieldValues(passport):
            result+=1

    return (result, EXPECTED_RESULT)

 
