import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    
    result = {}
    for tuple in getTuples_text(inputFile,  ' -> '):
        result[tuple[0]]='%s%s%s' % (tuple[0][0], tuple[1], tuple[0][1])

    return result


def solution(inputFile):

    steps = 40
    # template = 'NNCB'
    template = 'COPBCNPOBKCCFFBSVHKO'
    rules = getInputData(inputFile)

    ruleOccurences = {}

    for i in range(len(template)-1):
        ruleOccurences[template[i:i+2]] = 1

    # log(ruleOccurences)

    while steps>0:
        # log('step', steps)

        newRuleOccurences = {}

        for rule in ruleOccurences:
            # log('rule', rule)

            if ruleOccurences[rule] == 0:
                continue

            occurences = ruleOccurences[rule]

            if not rule in newRuleOccurences:
                newRuleOccurences[rule] = 0

            newRuleOccurences[rule] += occurences

            if rule in rules:
                newRuleOccurences[rule] -= occurences

                leftRule = rules[rule][0:2]
                rightRule = rules[rule][1:3]

                if not leftRule in newRuleOccurences:
                    newRuleOccurences[leftRule] = 0

                if not rightRule in newRuleOccurences:
                    newRuleOccurences[rightRule] = 0

                newRuleOccurences[leftRule] += occurences
                newRuleOccurences[rightRule] += occurences

        ruleOccurences = newRuleOccurences
        steps-=1

    # log(ruleOccurences, len(ruleOccurences))

    letterOccurences = {}

    letterOccurences[template[0]]=1
    letterOccurences[template[-1]]=1

    for rule in ruleOccurences:
        letter1 = rule[0]
        letter2 = rule[1]

        if not letter1 in letterOccurences:
            letterOccurences[letter1] = 0

        if not letter2 in letterOccurences:
            letterOccurences[letter2] = 0

        letterOccurences[letter1]+=ruleOccurences[rule]
        letterOccurences[letter2]+=ruleOccurences[rule]

    occurenceArray = [letterOccurences[rule] for rule in letterOccurences]

    occurenceArray.sort()

    result = int((occurenceArray[-1]-occurenceArray[0])/2)

    return (result,2942885922173)